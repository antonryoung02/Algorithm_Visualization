from manim import *
from RecursiveArray import RecursiveArray


class Recursion(VGroup):
    def __init__(self, scene, array, branching_factor=2, subproblem_size=2, **kwargs):
        super().__init__(**kwargs)
        self.array = array
        self.branching_factor = branching_factor
        self.level_spacing = 1.5  # Vertical spacing between levels
        self.subproblem_spacing = 1.5  # Base horizontal spacing between subproblems
        self.subproblem_size = subproblem_size
        self.root = None
        self.current_subproblem = None
        self.scene = scene

    def initial_animations(self):
        init_animations = self.divide_array(None, 0, 0, len(self.array))
        return init_animations

    def divide_array(self, parent, level, i, j):
        subproblem = RecursiveArray(
            self.scene, self.array[i:j], side_length=0.8, parent=parent
        )
        divide_animations = subproblem.initial_animations()

        if parent is not None:
            parent.children.append(subproblem)
            print(f"Parent: {parent.submobjects}")
        else:
            self.root = subproblem
            print("Parent: None")

        subproblem.parent = parent
        self.current_subproblem = subproblem
        self.add(subproblem)
        print(f"Subproblem: {subproblem.submobjects}")

        subproblem.move_to(self.calculate_position(level))
        if parent is not None:
            parent_arrow = CurvedArrow(
                parent.get_bottom(), subproblem.get_top(), angle=0
            )
            arrow_animation = subproblem.set_parent_arrow(parent_arrow)
            divide_animations.append(arrow_animation)

        return AnimationGroup(*divide_animations)

    def calculate_position(self, level):
        parent = self.current_subproblem.parent
        print(parent)
        if parent is None:
            # Position the root at the center
            return np.array([0, 3, 0])
        num_children_elements = len(self.array) / ((self.subproblem_size) ** (level))
        self.subproblem_spacing = 6 / (level + 1) ** 1.1

        # Calculate horizontal position relative to the parent
        # Assuming equal spacing between siblings
        total_sibling_width = 0.8 * num_children_elements
        start_x = parent.get_center()[0] - total_sibling_width / 2
        x = start_x + (
            1.2 * self.subproblem_spacing * ((len(parent.children) - 1)) / 1.3
        )

        # Calculate vertical position
        y = parent.get_center()[1] - self.level_spacing

        return np.array([x, y, 0])

    def traverse_up(self):
        parent = self.current_subproblem.parent
        if parent:
            new_arrow = CurvedArrow(
                self.current_subproblem.get_top(), parent.get_bottom(), angle=0
            )
            arrow_animation = self.current_subproblem.set_parent_arrow(new_arrow)
            self.current_subproblem = parent
            return arrow_animation

    def compare_equality_in_different_arrays(
        self, array1, array2, index1, index2, animation_length=0.1
    ):
        value1 = array1.elements[index1].value
        value2 = array2.elements[index2].value
        array1_animation = array1.compare_equality(index1, value2)
        array2_animation = array2.compare_equality(index2, value1)
        return Succession(
            AnimationGroup(array1_animation, array2_animation), Wait(animation_length)
        )

    def compare_size_in_different_arrays(
        self, array1, array2, index1, index2, animation_length=0.1
    ):
        value1 = array1.elements[index1].value
        value2 = array2.elements[index2].value
        array1_animation = array1.compare_size(index1, value2)
        array2_animation = array2.compare_size(index2, value1)
        return Succession(
            AnimationGroup(array1_animation, array2_animation), Wait(animation_length)
        )
