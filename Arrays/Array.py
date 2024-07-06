from manim import *
from Arrays.AbstractArray import AbstractArray
import copy

class Array(AbstractArray):
    """
    Array class, provides common array manipulation methods

    values: an array of strings, floats, or ints
    side_length: size of element boxes
    gap: distance between each element

    """

    def __init__(
        self,
        elements,
        **kwargs,
    ):        
        super().__init__(**kwargs)
        self.elements = [copy.deepcopy(element) for element in elements]

        self.element_length = 0.5
        self.gap = 0
        for index, element in enumerate(self.elements):
            if index == 0:
                self.add(element)
            else:
                self.add(
                    element.next_to(
                        self.elements[index - 1], RIGHT, buff=self.gap
                    )
                )
                
    def create(self) -> list[FadeIn]:
        """Returns a list of animations to play when the array is first created"""
        if len(self.elements) == 0:
            return Wait(0.1)
        return AnimationGroup(*[element.create() for element in self.elements])

    def insert_element(self, index, new_element, animation_length: float = 0.5) -> Succession:
        """Inserts an element at any index in the array"""
        self.elements.insert(index, new_element)
        if index != 0:
            new_element.next_to(self.elements[index - 1], RIGHT)
            shift_animations = self._shift_at_index(index, RIGHT)
        else:
            new_element.move_to(self.elements[0].get_center())
            shift_animations = self._shift_at_index(0, RIGHT)
        
        self.add(new_element)

        return Succession(shift_animations, FadeIn(new_element), Wait(animation_length))

    def remove_element(self, index,animation_length=0.5) -> Succession:
        """Deletes the element at the given index and shifts elements after index"""
        if index < 0 or index >= len(self.elements):
            return Succession(Wait(0.1))
        
        element = self.elements[index]
        shift_animations = self._shift_at_index(index, LEFT)
        self.remove(element)
        self.elements.pop(index)

        return Succession(
            AnimationGroup(shift_animations, element.delete()), Wait(animation_length)
        )

    def _shift_at_index(self, index: int, direction) -> AnimationGroup:
        """Helper method used in appending/deleting element."""
        shift_animations = [Wait(0.1)]
        for i in range(index, len(self)):
            shift_animations.append(self[i].animate.shift(direction * 2 * self.element_length + 2 * direction * self.gap))
        return AnimationGroup(*shift_animations)

    def __get_item__(self, index):
        return self.elements[index]

    def get_midpt(self):
        return (len(self.elements) - 1) // 2