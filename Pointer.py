from manim import *
import warnings
from Elements.Element import Element
from Arrays.Array import Array


class Pointer(VGroup):
    def __init__(
        self,
        scene: Scene,
        array_object: Array,
        initial_position: int,
        name: str,
        point_direction=UP,
        scale: float = 0.5,
        color: str = "#FF0000",
        show_text: bool = True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.array_object = array_object
        self.scene = scene
        self.position = initial_position
        self.point_direction = point_direction
        self.name = name
        self.color = color
        self.pointer_visual = None
        self.text_visual = None
        self.size = scale
        self.show_text = show_text

    def initialize(self) -> AnimationGroup:
        """Initializes visual and text, returns init animations"""
        self.pointer_visual = (
            Arrow(-1 * self.point_direction, self.point_direction, color=self.color)
            .scale(self.size)
            .next_to(
                self.array_object.elements[self.position], -1 * self.point_direction
            )
        )
        animations = []
        if self.show_text:
            self.text_visual = Text(
                f"{self.name} = {self.position}", color=self.color, font="Teko"
            ).scale(self.size)
            self.text_visual.next_to(
                self.array_object.elements[self.position], 4 * -1 * self.point_direction
            )
            animations.append(FadeIn(self.text_visual))
        animations.append(FadeIn(self.pointer_visual))
        return AnimationGroup(*animations)

    def update_position(
        self, new_position: int, animation_length: float = 0.1
    ) -> Succession:
        """Sets pointer index and returns moving animation"""
        if new_position == self.position:
            return Wait(0.1)
        if new_position < len(self.array_object.elements):
            animations = []
            new_location = self.pointer_visual.copy().next_to(
                self.array_object.elements[new_position], -1 * self.point_direction
            )
            self.position = new_position
            if self.show_text:
                animations.append(self.update_text_visual())

            animations.append(Transform(self.pointer_visual, new_location))
            return Succession(AnimationGroup(*animations), Wait(animation_length))
        else:
            warnings.warn(
                f"update_position called on new_position={new_position}, which is out of bounds for array length = {len(self.array_object.elements)}"
            )
            return Succession(Wait(0.1))

    def update_text_visual(self) -> MoveToTarget:
        """Updates pointer label and value and creates a movement animation."""
        text_str = f"{self.name} = {self.position}"
        updated_text_visual = Text(text_str, color=self.color, font="Teko").scale(
            self.size
        )

        self.text_visual.target = updated_text_visual
        self.text_visual.target.next_to(
            self.array_object.elements[self.position], 4 * -1 * self.point_direction
        )

        return MoveToTarget(self.text_visual)

    def delete(self, animation_length: float = 0.2) -> AnimationGroup:
        """Pointer removes itself from the scene"""
        animations = []
        if self.text_visual:
            animations.append(FadeOut(self.text_visual, run_time=animation_length))
        animations.append(FadeOut(self.pointer_visual, run_time=animation_length))
        return AnimationGroup(*animations)
