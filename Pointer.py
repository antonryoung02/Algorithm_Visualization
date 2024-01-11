from manim import *
import warnings


class Pointer(VGroup):
    def __init__(
        self,
        scene,
        elements,
        initial_position,
        name,
        scale=0.5,
        color="#FF0000",
        show_text=True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.elements = elements
        self.scene = scene
        self.position = initial_position
        self.name = name
        self.color = color
        self.pointer_visual = None
        self.text_visual = None
        self.size = scale
        self.show_text = show_text

    def initialize(self):
        self.pointer_visual = (
            Arrow(DOWN, UP, color=self.color)
            .scale(self.size)
            .next_to(self.elements[self.position], DOWN)
        )
        animations = []
        if self.show_text:
            self.text_visual = Text(
                f"{self.name} = {self.position}", color=self.color, font="Teko"
            ).scale(self.size)
            self.text_visual.next_to(self.elements[self.position], 4 * DOWN)
            animations.append(FadeIn(self.text_visual))
        animations.append(FadeIn(self.pointer_visual))
        return AnimationGroup(*animations)

    def update_position(self, new_position, animation_length=0.1):
        if new_position == self.position:
            return Wait(0.1)
        if new_position < len(self.elements):
            animations = []
            new_location = self.pointer_visual.copy().next_to(
                self.elements[new_position], DOWN
            )
            self.position = new_position
            if self.show_text:
                animations.append(self.update_text_visual())

            animations.append(Transform(self.pointer_visual, new_location))
            return Succession(AnimationGroup(*animations), Wait(animation_length))
        else:
            warnings.warn(
                f"update_position called on new_position={new_position}, which is out of bounds for array length = {len(self.elements)}"
            )
            return Wait(0.1)

    def update_text_visual(self):
        """Updates pointer label and value and creates a movement animation."""
        text_str = f"{self.name} = {self.position}"
        updated_text_visual = Text(text_str, color=self.color, font="Teko").scale(
            self.size
        )

        self.text_visual.target = updated_text_visual
        self.text_visual.target.next_to(self.elements[self.position], 4 * DOWN)

        return MoveToTarget(self.text_visual)

    def delete(self, animation_length=0.2):
        animations = []
        if self.text_visual:
            animations.append(FadeOut(self.text_visual, run_time=animation_length))
        animations.append(FadeOut(self.pointer_visual, run_time=animation_length))
        return AnimationGroup(*animations)

    def array_changed(self, new_elements, animation_length=0.3):
        self.elements = new_elements
