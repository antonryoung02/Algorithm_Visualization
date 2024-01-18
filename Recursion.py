from manim import *
from RecursiveArray import RecursiveArray


# FIX! array.stack_direction only works for RIGHT
class Recursion(VGroup):
    def __init__(
        self,
        scene: Scene,
        array: list,
        branching_factor: int = 2,
        subproblem_size: int = 2,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.array = array
        self.branching_factor = branching_factor
        self.level_spacing = 1.5  # Vertical spacing between levels
        self.subproblem_spacing = 1.5  # Base horizontal spacing between subproblems
        self.subproblem_size = subproblem_size
        self.root = None
        self.current_subproblem = None
        self.scene = scene

    def initialize_array(self) -> AnimationGroup:
        init_animations = self.divide_array(None, 0, 0, len(self.array))
        return init_animations

    def set_current_subproblem(self, new_current_subproblem):
        self.current_subproblem = new_current_subproblem

    def divide_array(
        self, parent: RecursiveArray, level: int, i: int, j: int
    ) -> AnimationGroup:
        """Recursive divide step, displaying new array made from array[i:j]"""
        subproblem = RecursiveArray(
            self.scene, self.array[i:j], side_length=0.8, parent=parent
        )
        divide_animations = subproblem.initial_animations()
        self.set_current_subproblem(subproblem)
        self.add(subproblem)
        subproblem.move_to(self._calculate_position(level))

        if parent is not None:
            parent.children.append(self.current_subproblem)
            arrow_animation = self._create_curved_arrow(
                parent, self.current_subproblem, 0.0
            )
            divide_animations.append(arrow_animation)
        else:
            self.root = self.current_subproblem

        return AnimationGroup(*divide_animations)

    def _create_curved_arrow(
        self, start_element: RecursiveArray, end_element: RecursiveArray, angle: float
    ) -> AnimationGroup:
        parent_arrow = CurvedArrow(
            start_point=start_element.get_bottom(),
            end_point=end_element.get_top(),
            angle=angle,
        )
        end_element.set_parent_arrow(parent_arrow)
        arrow_animation = AnimationGroup(FadeIn(parent_arrow))
        return arrow_animation

    def _calculate_position(self, level: int):
        parent = self.current_subproblem.parent
        if parent is None:
            return np.array([0, 3, 0])  # Root positioning in top center

        num_children_elements = len(self.array) / ((self.subproblem_size) ** (level))
        self.subproblem_spacing = 6 / (level + 1) ** 1.1

        total_sibling_width = 0.8 * num_children_elements
        start_x = parent.get_center()[0] - total_sibling_width / 2
        x = start_x + (1.2 * self.subproblem_spacing * ((len(parent.children))) / 1.3)

        y = parent.get_center()[1] - self.level_spacing

        return np.array([x, y, 0])

    def traverse_up(self) -> AnimationGroup:
        """Emulates the upwards traversal of a recursive return statement. Use before returning in base case or inductive step."""
        completed_animations = self.current_subproblem.show_completed()
        parent = self.current_subproblem.parent
        if parent:  # Could give to .set_parent_arrow or RecursiveArray class
            new_arrow = CurvedArrow(
                start_point=self.current_subproblem.get_top(),
                end_point=parent.get_bottom(),
                angle=0.0,
            )
            arrow_animation = self.current_subproblem.set_parent_arrow(new_arrow)
        self.current_subproblem = parent
        return AnimationGroup(completed_animations, arrow_animation)

    def compare_equality_in_different_arrays(
        self,
        array1: RecursiveArray,
        array2: RecursiveArray,
        index1: int,
        index2: int,
        animation_length: float = 0.1,
    ) -> Succession:
        """Displays a compare_equality animation at the indices in both lists. Useful during combine step calculations"""
        value1 = array1.elements[index1].value
        value2 = array2.elements[index2].value
        array1_animation = array1.compare_equality(index1, value2)
        array2_animation = array2.compare_equality(index2, value1)
        return Succession(
            AnimationGroup(array1_animation, array2_animation), Wait(animation_length)
        )

    def compare_size_in_different_arrays(
        self,
        array1: RecursiveArray,
        array2: RecursiveArray,
        index1: int,
        index2: int,
        animation_length: float = 0.1,
    ) -> Succession:
        """Displays a compare_size animation at the indices in both lists. Useful during combine step calculations"""
        value1 = array1.elements[index1].value
        value2 = array2.elements[index2].value
        array1_animation = array1.compare_size(index1, value2)
        array2_animation = array2.compare_size(index2, value1)
        return Succession(
            AnimationGroup(array1_animation, array2_animation), Wait(animation_length)
        )
