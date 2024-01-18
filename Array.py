from manim import *
from Element import Element


class Array(VGroup):
    """
    Array class, provides common array manipulation methods

    values: an array of strings, floats, or ints
    side_length: size of element boxes
    gap: distance between each element

    """

    # Is scene really necessary?
    def __init__(
        self,
        scene,
        values,
        stack_direction=RIGHT,
        side_length: float = 1.5,
        gap: float = 0.0,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.scene = scene
        self.array: List[int] = values
        self.elements: [Element] = [Element(value, side_length) for value in values]
        self.gap: float = gap
        self.side_length = side_length
        self.stack_direction = stack_direction

        self.initialize()

    def initialize(self) -> None:
        """Creates element objects for every element in the array"""
        for index, element in enumerate(self.elements):
            if index == 0:
                self.add(element)
            else:
                self.add(
                    element.next_to(
                        self.elements[index - 1], self.stack_direction, buff=self.gap
                    )
                )

    def initial_animations(self) -> list[FadeIn]:
        """Returns a list of animations to play when the array is first created"""
        return [FadeIn(element) for element in self.elements]

    def append(self, value: any, animation_length: float = 0.5) -> Succession:
        """Appends a new element to the end of the array"""
        new_element = Element(value, self.side_length)
        if self.elements:
            new_element.next_to(self.elements[-1], self.stack_direction, buff=self.gap)
        self.elements.append(new_element)
        self.add(new_element)
        return Succession(FadeIn(new_element), Wait(animation_length))

    # Can refactor to insert at index, LinkedList insert method
    def prepend(self, value: any, animation_length: float = 0.5) -> Succession:
        """Prepends a new element to the beginning of the array"""
        new_element = Element(value)
        new_element.move_to(self.elements[0].get_center())

        shift_animations = self._shift_at_index(0, self.side_length + self.gap)

        self.elements.insert(0, new_element)
        self.add(new_element)
        return Succession(
            AnimationGroup(*shift_animations, FadeIn(new_element)),
            Wait(animation_length),
        )

    def _is_index_invalid(self, index):
        """Used to return early if index causes out of bounds error"""
        if 0 <= index < len(self.array):
            return False
        print(f"recieved invalid index {index} for array of length {len(self.array)}")
        return True

    def _shift_at_index(self, index: int, distance: float) -> list:
        """Helper method used in appending element."""
        shift_animations = []
        if self._is_index_invalid(index):
            return [shift_animations]
        for i in range(index, len(self)):
            shift_animations.append(
                self[i].animate.shift(self.stack_direction * distance)
            )
        return [shift_animations]

    def swap(
        self, index1: int, index2: int, animation_length: float = 0.2
    ) -> Succession:
        """Visually swaps the elements at the given indexes"""
        if self._is_index_invalid(index1) or self._is_index_invalid(index2):
            return Succession(Wait(0.1))
        elem1, elem2 = self.elements[index1], self.elements[index2]
        anim1 = elem1.animate.move_to(elem2.get_center())
        anim2 = elem2.animate.move_to(elem1.get_center())
        self.elements[index1], self.elements[index2] = elem2, elem1
        return Succession(AnimationGroup(anim1, anim2), Wait(animation_length))

    def compare_equal_at_index(
        self,
        index1: int,
        index2: int,
        equal_colors: str = "#00FF00",
        unequal_colors: str = "#FF0000",
    ) -> Succession:
        """Visually compares the elements at the given indices"""
        if self._is_index_invalid(index1) or self._is_index_invalid(index2):
            return Succession(Wait(0.1))
        element1 = self.elements[index1]
        element2 = self.elements[index2]
        boundary_color = (
            equal_colors if element1.value == element2.value else unequal_colors
        )

        boundary1 = AnimatedBoundary(
            element1.square, colors=[boundary_color], cycle_rate=3
        )
        boundary2 = AnimatedBoundary(
            element2.square, colors=[boundary_color], cycle_rate=3
        )
        return Succession(
            FadeIn(boundary1, boundary2), Wait(0.1), FadeOut(boundary1, boundary2)
        )

    def compare_value_equal(
        self, index, val, equal_colors="#00FF00", unequal_colors="#FF0000"
    ) -> Succession:
        """Visually compares the element at the given index to the given value"""
        element = self.elements[index]
        boundary_color = equal_colors if element.value == val else unequal_colors

        boundary = AnimatedBoundary(element.square, colors=boundary_color, cycle_rate=3)

        return Succession(FadeIn(boundary), FadeOut(boundary))

    def compare_size(self, index, val) -> Succession:
        """Visually compares the element at the given index to the given value"""
        if self._is_index_invalid(index):
            return Succession(Wait(0.1))
        element = self.elements[index]

        if element.value < val:
            text_animation = ScaleInPlace(element.text, 0.5)
            scale_back_animation = ScaleInPlace(element.text, 2)
        else:
            text_animation = ScaleInPlace(element.text, 1.5)
            scale_back_animation = ScaleInPlace(element.text, 2 / 3)

        return Succession(text_animation, scale_back_animation)

    def compare_size_at_index(self, index1, index2) -> Succession:
        """Visually compares the elements at the given indices"""
        element1 = self.elements[index1]
        element2 = self.elements[index2]

        if element1.value < element2.value:
            smaller_text_animation = ScaleInPlace(element1.text, 0.5)
            larger_text_animation = ScaleInPlace(element2.text, 1.5)
            scale_back_smaller = ScaleInPlace(element1.text, 2)
            scale_back_larger = ScaleInPlace(element2.text, 2 / 3)
        else:
            smaller_text_animation = ScaleInPlace(element2.text, 0.5)
            larger_text_animation = ScaleInPlace(element1.text, 1.5)
            scale_back_smaller = ScaleInPlace(element2.text, 2)
            scale_back_larger = ScaleInPlace(element1.text, 2 / 3)

        scaling_animations = AnimationGroup(
            smaller_text_animation, larger_text_animation
        )
        scale_back_animations = AnimationGroup(scale_back_smaller, scale_back_larger)

        return Succession(scaling_animations, scale_back_animations)

    def delete(self, index, side_length=1.5, animation_length=0.5) -> Succession:
        """Deletes the element at the given index and shifts elements after index"""
        if self._is_index_invalid(index):
            return Succession(Wait(0.1))
        element = self.elements[index]
        shift_animations = []
        for i in range(index + 1, len(self.elements)):
            shift_animations.append(
                self.elements[i].animate.shift(-1 * self.stack_direction * side_length)
            )
        self.remove(element)

        self.elements = [elem for i, elem in enumerate(self.elements) if i != index]

        return Succession(
            AnimationGroup(*shift_animations, FadeOut(element)), Wait(animation_length)
        )

    def get_length(self) -> int:
        return len(self.elements)

    def change_value(
        self, index: int, new_val: any
    ) -> AnimationGroup:  # Todo add visible animation
        """Visibly changes the element's value at index"""
        if self._is_index_invalid(index):
            return AnimationGroup(Wait(0.1))
        return AnimationGroup(self.elements[index].set_value(new_val))

    def clear_array(self) -> AnimationGroup:
        """Clears array"""
        animations = []
        for element in self.elements:
            animations.append(element.set_value(""))
        return AnimationGroup(*animations)
