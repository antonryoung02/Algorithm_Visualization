from manim import *

class Pointer(VGroup):
    def __init__(self, array, direction, style, name=None, **kwargs):
        super().__init__(**kwargs)
        self.array = array
        self.direction = direction
        self._scale = 0.4
        self.name = name
        self.pointer = Arrow(-1 * direction, direction).scale(self._scale)
        self.current_element = None
        self.text = None
        self.add(self.pointer)
        self.set_style(style)

    def create(self, index=0) -> AnimationGroup:
        """Initializes visual and text, returns init animations"""
        element = self.array.get_element_at_index(index)
        self.pointer.next_to(element, -1 * self.direction, buff=0)
        
        if self.name is not None:
            text_content = f"{self.name}: {index}" 
        else:
            text_content = ""

        self.text = Text(text_content, font_size=18, color=self.pointer.get_color()).next_to(element, -1 * self.direction, buff=0.7)

        self.add(self.text)
        return AnimationGroup(FadeIn(self.pointer), FadeIn(self.text))
    
    def set_style(self, style):
        new_pointer = Arrow(-1*self.direction, self.direction, **style).scale(self._scale).move_to(self.pointer, -1 * self.direction)
        pointer_transform = ReplacementTransform(self.pointer, new_pointer)
        self.remove(self.pointer)
        self.add(new_pointer)
        self.pointer = new_pointer

        return pointer_transform

    def update(self, index: int):
        """Sets pointer index and returns moving animation"""
        visit_end_animations = Wait(0.1)
        if self.current_element:
            visit_end_animations = self.current_element.call_callback_hooks("on_visit_end")

        if self.name is not None:
            text_content = f"{self.name}: {index}" 
        else:
            text_content = ""

        self.current_element = self.array.get_element_at_index(index)
        if self.current_element is None:
            new_text = Text(text_content, font_size=18, color=self.pointer.get_color()).move_to(self.text)
            text_animation = ReplacementTransform(self.text, new_text)
            self.text = new_text
            return Succession(visit_end_animations, text_animation)

        pointer_animation = self.pointer.animate.next_to(self.current_element, -1 * self.direction, buff=0)
        visit_start_animations = self.current_element.call_callback_hooks("on_visit_start")
        new_text = Text(text_content, font_size=18, color=self.pointer.get_color()).next_to(self.current_element, -1 * self.direction, buff=0.7)
        text_animation = ReplacementTransform(self.text, new_text)
        self.text = new_text
        return Succession(visit_end_animations, AnimationGroup(pointer_animation, text_animation), visit_start_animations)

    def delete(self) -> AnimationGroup:
        """Pointer removes itself from the scene"""
        visit_end_animations = Wait(0.1)
        if self.current_element:
            visit_end_animations = self.current_element.call_callback_hooks("on_visit_end")
        if self.text:
           return AnimationGroup(FadeOut(self.pointer), FadeOut(self.text), visit_end_animations) 
        
        return AnimationGroup(FadeOut(self.pointer), visit_end_animations)
