from manim import * 

class Pointer(VGroup):
    def __init__(self, scene, elements, initial_position, name, color="#FF0000", **kwargs):
        super().__init__(**kwargs)
        self.elements = elements
        self.scene = scene
        self.position = initial_position
        self.name = name
        self.color = color
        self.pointer_visual = None
        self.text_visual = None

    def initialize(self):
        self.pointer_visual = Arrow(DOWN, UP, color=self.color).scale(0.5)
        animation = self.pointer_visual.next_to(self.elements[self.position], DOWN)
        self.text_visual = Text(f"{self.name} = {self.position}", color=self.color, font="Teko").scale(0.5)
        self.text_visual.next_to(self.elements[self.position], 4*DOWN)
        self.scene.play(FadeIn(animation), FadeIn(self.text_visual))
        self.scene.wait(0.5)

    def update_position(self, new_position, animation_length=0.3):
        if new_position < len(self.elements):
            new_location = self.pointer_visual.copy().next_to(self.elements[new_position], DOWN)
            self.position = new_position
            text_animation = self.update_text_visual()
            self.scene.play(Transform(self.pointer_visual, new_location), text_animation)
            self.scene.wait(animation_length)
        else:
            print(f"update_position called on new_position {new_position}, which is out of bounds for array length {len(self.elements)}")

    def update_text_visual(self):
        """Updates pointer label and value and creates a movement animation."""
        text_str = f"{self.name} = {self.position}"
        updated_text_visual = Text(text_str, color=self.color, font="Teko").scale(0.5)

        self.text_visual.target = updated_text_visual
        self.text_visual.target.next_to(self.elements[self.position], 4*DOWN)

        return MoveToTarget(self.text_visual)

    def delete(self, animation_length=0.2):
        if self.text_visual:
            self.scene.remove(self.text_visual)
        self.scene.remove(self.pointer_visual)
        self.scene.wait(animation_length)

    def array_changed(self, new_elements, animation_length=0.3):
        self.elements = new_elements






    