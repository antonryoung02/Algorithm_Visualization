from manim import *
from Arrays.Array import Array
from Elements.Element import Element


# Fix: Not returning animations
# Think about adding attributes for arrow and .next in element so that arrows aren't in the array and are easily accessible
class LinkedList(Array):
    def __init__(self, scene, array, side_length=1.5, arrow_length=0.6):
        super().__init__(scene, array, side_length, gap=0)
        self.arrow_length = arrow_length

    def initialize(self):
        self.add(self.elements[0])
        arrow = Arrow(LEFT, RIGHT).scale(0.4).next_to(self[0], RIGHT, buff=0)
        self.add(arrow)
        for index in range(1, len(self.elements)):
            current_element = self.elements[index].next_to(
                self[2 * index - 1], RIGHT, buff=self.gap
            )
            self.add(current_element)
            if index != len(self.elements) - 1:
                arrow = (
                    Arrow(LEFT, RIGHT)
                    .scale(0.4)
                    .next_to(self[2 * index], RIGHT, buff=0)
                )
                self.add(arrow)

    def initial_animations(self):
        return [FadeIn(obj) for obj in self]

    def unlink(self, index):
        unlink_current_element_animations = []
        link_next_element_animations = []
        element_pos = 2 * index
        element = self[element_pos]

        if index > 0 and element_pos + 2 < len(self):
            prev_arrow = self[element_pos - 1]
            next_element = self[element_pos + 2]

            stretched_arrow = CurvedArrow(
                self[element_pos - 2].get_corner(DR),
                next_element.get_corner(DL),
                angle=TAU / 2.8,
            )
            unlink_current_element_animations.append(
                Transform(prev_arrow, stretched_arrow)
            )

            original_arrow_shape = CurvedArrow(
                self[element_pos - 2].get_right(), element.get_left(), angle=0
            )
            link_next_element_animations.append(
                Transform(prev_arrow, original_arrow_shape)
            )

        return unlink_current_element_animations, link_next_element_animations

    def delete(self, index, animation_length=1):
        # Validate index
        if index < 0 or index >= self.get_length():
            return None

        element_pos = 2 * index
        element = self[element_pos]
        shift_animations = []
        unlink_current_element, link_next_element = self.unlink(index)

        total_shift_distance = self.side_length + self.arrow_length

        for i in range(2 * (index + 1), len(self)):
            shift_animations.append(self[i].animate.shift(LEFT * total_shift_distance))

        arrow_to_remove = None
        if element_pos == len(self) - 1:
            arrow_to_remove = self[element_pos - 1]
            self.remove(arrow_to_remove)
        else:
            arrow_to_remove = self[element_pos + 1]
            self.remove(arrow_to_remove)

        self.remove(element)
        self.elements = [elem for i, elem in enumerate(self.elements) if i != index]

        animations = [FadeOut(element)] + shift_animations
        if arrow_to_remove is not None:
            animations.append(FadeOut(arrow_to_remove))
        self.scene.play(AnimationGroup(*unlink_current_element, lag_ratio=1))
        self.scene.wait(animation_length / 2)
        self.scene.play(AnimationGroup(*animations, *link_next_element))
        self.scene.wait(animation_length / 2)

    def append(self, value):
        pass

    def prepend(self, value):
        pass

    def insert(self, index, value, animation_length=1):
        new_element = Element(value, side_length=self.side_length)
        new_arrow = Arrow(LEFT, RIGHT).scale(0.4)

        insert_animations = []
        if index == 0:
            new_element.move_to(self[0])
            new_arrow.next_to(new_element, RIGHT, buff=0)
            shift_animations = self._shift_at_index(
                index * 2, self.side_length + self.arrow_length
            )
            self.submobjects = [new_element, new_arrow] + self.submobjects
            self.elements = [new_element] + self.elements

        elif index == self.get_length() - 1:
            # Insert at the end
            new_arrow.next_to(self[-1], RIGHT, buff=0)
            new_element.next_to(new_arrow, RIGHT, buff=0)
            shift_animations = []
            self.submobjects += [new_arrow, new_element]
            self.elements += [new_element]

        else:
            # New element appears below its index
            new_element.next_to(self[index * 2], DOWN, buff=0.3)
            # Previous arrow points to this new element
            animation_prev_arrow = CurvedArrow(
                self[2 * (index - 1)].get_right(), new_element.get_left(), angle=0
            )
            # new arrow points upwards to its index
            new_arrow = CurvedArrow(
                new_element.get_top(), self[index * 2].get_bottom(), angle=0
            )

            insert_animations.append(FadeIn(new_element))
            insert_animations.append(
                Transform(self[2 * index - 1], animation_prev_arrow)
            )
            insert_animations.append(FadeIn(new_arrow))

            shift_animations = self._shift_at_index(
                index * 2, self.side_length + self.arrow_length
            )
            insertion_index = (
                index * 2
            )  # Each element has an element and an arrow, so we multiply the index by 2
            shift_animations.append(
                Transform(
                    self[2 * index - 1],
                    Arrow(LEFT, RIGHT)
                    .scale(0.4)
                    .next_to(self[2 * index - 2], RIGHT, buff=0),
                )
            )
            shift_animations.append(
                new_element.animate.next_to(self[index * 2 - 1], RIGHT, buff=0)
            )
            shift_animations.append(
                Transform(
                    new_arrow,
                    Arrow(LEFT, RIGHT)
                    .scale(0.4)
                    .next_to(self[2 * index], RIGHT, buff=0),
                )
            )
            self.submobjects = (
                self.submobjects[:insertion_index]
                + [new_element, new_arrow]
                + self.submobjects[insertion_index:]
            )
            self.elements = (
                self.elements[:index] + [new_element] + self.elements[index:]
            )

            self.scene.play(AnimationGroup(*insert_animations))
            self.scene.wait(animation_length / 2)
            self.scene.play(AnimationGroup(*shift_animations))
            self.scene.wait(animation_length / 2)
            return
        self.scene.play(AnimationGroup(*insert_animations))
        self.scene.wait(animation_length / 2)
        self.scene.play(
            AnimationGroup(*shift_animations, FadeIn(new_element), FadeIn(new_arrow))
        )
        self.scene.wait(animation_length / 2)
        return
