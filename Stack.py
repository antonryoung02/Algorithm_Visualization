from manim import *
from Array import Array
from Element import Element


class Stack(Array):
    def __init__(
        self, scene, values, side_length=1.5, stack_direction=UP, gap=0.0, **kwargs
    ):
        super().__init__(scene, values, stack_direction, side_length, gap, **kwargs)

    def _get_start_position(self):
        # Compare using numpy array equality and then use all() to check if all elements are equal
        if np.all(self.stack_direction == UP):
            return 3 * RIGHT
        elif np.all(self.stack_direction == DOWN):
            return 3 * LEFT
        elif np.all(self.stack_direction == LEFT):
            return 3 * DOWN
        elif np.all(self.stack_direction == RIGHT):
            return 3 * UP
        else:
            return 3 * RIGHT  # Default direction

    def push(self, value, animation_length=0.5):
        new_element = Element(value, self.side_length)
        start_position = self._get_start_position()
        new_element.move_to(start_position)

        if self.elements:
            target_position = self.elements[-1].get_center() + self.stack_direction * (
                self.side_length + self.gap
            )
        else:
            target_position = self.scene.get_center()

        new_element.generate_target()
        new_element.target.move_to(target_position)
        fly_in_and_stack = MoveToTarget(new_element, run_time=animation_length)
        self.elements.append(new_element)
        self.scene.add(new_element)

        return Succession(fly_in_and_stack, Wait(animation_length))

    def pop(self, animation_length=0.5):
        return self.delete(self.get_length() - 1, animation_length)

    def peek(self, animation_length=0.5):
        return self.compare_size(self.get_length() - 1, -9999)
