from manim import *

class Pointer(VGroup):
    def __init__(self, array, direction, style, name=None, **kwargs):
        super().__init__(**kwargs)
        self.array = array
        self.direction = direction
        self._scale = 0.4
        self.name = name
        self.pointer = Arrow(-1 * direction, direction).scale(self._scale)
        self.text = None
        self.add(self.pointer)
        self.set_style(style)

    def create(self, index=0) -> AnimationGroup:
        """Initializes visual and text, returns init animations"""
        element = self.array.get_element_at_index(index)
        self.pointer.next_to(element, -1 * self.direction, buff=0)
        self.text = Text(f"{self.name}: {index}", font_size=18, color=self.pointer.get_color()).next_to(element, -1 * self.direction, buff=0.7)

        self.add(self.text)
        return FadeIn(self.pointer)
    
    def set_style(self, style):
        new_pointer = Arrow(-1*self.direction, self.direction, **style).scale(self._scale).move_to(self.pointer, -1 * self.direction)
        pointer_transform = ReplacementTransform(self.pointer, new_pointer)
        self.remove(self.pointer)
        self.add(new_pointer)
        self.pointer = new_pointer

        return pointer_transform

    def update(self, index: int):
        """Sets pointer index and returns moving animation"""
        element = self.array.get_element_at_index(index)
        if element == -1:
            return Wait(0.1)
    
        pointer_animation = self.pointer.animate.next_to(element, -1 * self.direction, buff=0)
        new_text = Text(f"{self.name}: {index}", font_size=18, color=self.pointer.get_color()).next_to(element, -1 * self.direction, buff=0.7)
        text_animation = ReplacementTransform(self.text, new_text)
        self.text = new_text
        return AnimationGroup(pointer_animation, text_animation)

    def delete(self) -> AnimationGroup:
        """Pointer removes itself from the scene"""
        return FadeOut(self.pointer)
