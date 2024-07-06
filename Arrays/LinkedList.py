from manim import *
from Arrays.Array import Array
from Arrays.AbstractArray import AbstractArray
from Elements.Element import Element

class LinkedList(AbstractArray):
    def __init__(self, elements, **kwargs):
        super().__init__(**kwargs)
        self.elements = []
        self.element_length = 1
        self.gap=0

        for index, element in enumerate(elements):
            self.elements.append(element)
            if index == 0:
                self.add(element)
            else:
                self.add(element.next_to(self[-1], RIGHT, buff=0))
            
            if index != len(elements) - 1:
                arrow = Arrow(LEFT, RIGHT).scale(0.4)
                self.elements.append(arrow)
                self.add(arrow.next_to(self[-1], RIGHT, buff=0))

    def create(self):
        if len(self.elements) == 0:
            return Wait(0)
        return AnimationGroup(*[FadeIn(obj) for obj in self.elements])

    def _unlink(self, index):
        element_pos = 2 * index
        element = self.elements[element_pos]

        if index > 0 and element_pos + 2 < len(self):
            prev_arrow = self.elements[element_pos - 1]
            next_element = self.elements[element_pos + 2]

            stretched_arrow = CurvedArrow(
                self.elements[element_pos - 2].get_corner(DR),
                next_element.get_corner(DL),
                angle=TAU / 2.8,
            )
            unlink_current_element = Transform(prev_arrow, stretched_arrow)

            original_arrow_shape = CurvedArrow(
                self.elements[element_pos - 2].get_right(), element.get_left(), angle=0
            )
            link_next_element = Transform(prev_arrow, original_arrow_shape)
            return unlink_current_element, link_next_element
        else:
            return Wait(0), Wait(0)

    def remove_element(self, index, animation_length=1):
        # Validate index
        if index < 0 or 2 * index >= len(self.elements):
            return None

        element_pos = 2 * index
        element = self.elements[element_pos]
        unlink_current_element, link_next_element = self._unlink(index)

        shift_animations = [self._shift_at_index(2*index, LEFT)]
        if element_pos == len(self) - 1:
            arrow_to_remove = self.elements[element_pos - 1]
            self.remove(arrow_to_remove)
            self.elements.pop(element_pos)
            self.elements.pop(element_pos - 1)
        else:
            arrow_to_remove = self.elements[element_pos + 1]
            self.remove(arrow_to_remove)
            self.elements.pop(element_pos + 1)
            self.elements.pop(element_pos)

        self.remove(element)
        shift_animations.append(element.delete())
        shift_animations.append(FadeOut(arrow_to_remove))
        
        return Succession(unlink_current_element, AnimationGroup(*shift_animations, link_next_element))
    
    def change_element(
        self, index: int, data=None, style=None
    ) -> AnimationGroup:
        """Visibly changes the element's value at index"""
        if index < 0 or index >= (len(self.elements) / 2):
            return AnimationGroup(Wait(0))
        animations = []
        if data:
            animations.append(self.elements[2*index].set_data(data))
        if style:
            animations.append(self.elements[2*index].set_style(style))

        return AnimationGroup(*animations)
    
    def _shift_at_index(self, index: int, direction) -> AnimationGroup:
        """Helper method used in appending/deleting element."""
        shift_animations = [Wait(0)]
        shift_distance = 1.6
        for i in range(index, len(self.elements)):
            shift_animations.append(self.elements[i].animate.shift(direction * shift_distance + 2 * direction * self.gap))
        return AnimationGroup(*shift_animations)
    
    def insert_element(self, index, new_element):
        new_arrow = Arrow(LEFT, RIGHT).scale(0.4) # Extend to direction??
        
        if index == (len(self.elements) - 1) / 2:
            new_arrow.next_to(self.elements[-1], RIGHT, buff=0)
            new_element.next_to(new_arrow, RIGHT, buff=0)
            animations = AnimationGroup(new_element.create(), FadeIn(new_arrow))
            self.add(new_element)
            self.add(new_arrow)
            self.elements.append(new_arrow)
            self.elements.append(new_element)
            return animations

        elif index == 0:
            new_element.next_to(self.elements[2 * index], DOWN, buff=0.3)
            new_arrow.next_to(new_element, UP, buff=0)
            new_arrow = CurvedArrow(new_element.get_top(), self.elements[index * 2].get_bottom(), angle=0)

            step_one_animations = AnimationGroup(FadeIn(new_element), FadeIn(new_arrow))
            move_element_in_place = new_element.animate.move_to(self[0])
            shift_elements_down = self._shift_at_index(0, RIGHT)
            move_new_arrow = Transform(new_arrow, Arrow(LEFT, RIGHT).scale(0.4).next_to(self.elements[2 * index], RIGHT, buff=0))
            step_two_animations = AnimationGroup(shift_elements_down, move_element_in_place, move_new_arrow)
        else:
            new_element.next_to(self.elements[2 * index], DOWN, buff=0.3)
            animation_prev_arrow = CurvedArrow(self.elements[2 * (index - 1)].get_right(), new_element.get_left(), angle=0)
            new_arrow = CurvedArrow(new_element.get_top(), self.elements[index * 2].get_bottom(), angle=0)

            step_one_animations = AnimationGroup(FadeIn(new_element), Transform(self.elements[2 * index - 1], animation_prev_arrow), FadeIn(new_arrow))
            shift_elements_down = self._shift_at_index(index * 2, RIGHT)
            move_prev_arrow = Transform(self.elements[2 * index - 1], Arrow(LEFT, RIGHT).scale(0.4).next_to(self.elements[2 * index - 2], RIGHT, buff=0))
            move_element_in_place = new_element.animate.next_to(self.elements[index * 2 - 1], RIGHT, buff=0)
            move_new_arrow = Transform(new_arrow, Arrow(LEFT, RIGHT).scale(0.4).next_to(self.elements[2 * index], RIGHT, buff=0))
            step_two_animations = AnimationGroup(shift_elements_down, move_prev_arrow, move_element_in_place, move_new_arrow)

        self.add(new_element)
        self.add(new_arrow)
        self.elements.insert(2 * index, new_element)
        self.elements.insert(2 * index + 1, new_arrow)

        return Succession(step_one_animations, Wait(0.2), step_two_animations)
