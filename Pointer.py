from manim import * 

class Pointer(VGroup):
    def __init__(self, array, scene, initial_position, name, text_color="#FF0000", **kwargs):
        super().__init__(**kwargs)
        self.array = array
        self.scene = scene
        self.position = initial_position
        self.name = name
        self.pointer_visual = None
        self.text_color = text_color
        self.text_visual = None

    def initialize(self):
        self.pointer_visual = Arrow(DOWN, UP, color=self.text_color).scale(0.5)
        animation = self.pointer_visual.next_to(self.array[self.position], DOWN)
        return FadeIn(animation)

    def update_position(self, new_position):
        new_location = self.pointer_visual.copy().next_to(self.array[new_position], DOWN)
        self.position = new_position
        self.update_display_name()
        return AnimationGroup(Transform(self.pointer_visual, new_location), Write(self.text_visual))
    
    def update_display_name(self):
        """Displays pointer label and value"""
        text_str = f"{self.name} = {self.position}"

        if self.text_visual:
            self.scene.remove(self.text_visual)

        self.text_visual = Text(text_str, color=self.text_color, font="Teko").scale(0.5)
        self.text_visual.next_to(self.pointer_visual, RIGHT)

        self.scene.add(self.text_visual)

        return self.text_visual

    def delete(self):
        if self.text_visual:
            self.scene.remove(self.text_visual)
        self.scene.remove(self.pointer_visual)
        self.scene.wait(0.1)  






    