from manim import *
from Arrays.RecursiveArray import RecursiveArray
from Elements.TreeElement import TreeElement

class Recursion(VGroup):
    def __init__(
        self,
        elements,
        branching_factor: int = 2,
        subproblem_size: int = 2,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.elements = list(elements)
        self.branching_factor = branching_factor
        self.level_spacing = 1.5  # Vertical spacing between levels
        self.subproblem_spacing = 1.5  # Base horizontal spacing between subproblems
        self.subproblem_size = subproblem_size
        self.root = None
        self.current_subproblem = None

    def initialize(self) -> AnimationGroup:
        return self.divide_array(None, 0, 0, len(self.elements))

    def divide_array(
        self, parent: RecursiveArray, level: int, i: int, j: int
    ) -> AnimationGroup:
        """Recursive divide step, displaying new array made from array[i:j]"""
        subproblem = RecursiveArray(self.elements[i:j], parent=parent)
        
        self.current_subproblem = subproblem
        self.current_subproblem.move_to(self._calculate_position(level))

        self.add(self.current_subproblem)

        if parent is not None:
            parent.children.append(self.current_subproblem)
            parent_arrow = CurvedArrow(start_point=parent.get_bottom(),end_point=self.current_subproblem.get_top(),angle=0)
            arrow_animation = self.current_subproblem.set_parent_arrow(parent_arrow)
        else:
            self.root = self.current_subproblem
            arrow_animation = Wait(0.1)

        return AnimationGroup(self.current_subproblem.create(), arrow_animation)

    def _create_curved_arrow(
        self, start: RecursiveArray, end: RecursiveArray, angle: float
    ) -> AnimationGroup:
        parent_arrow = CurvedArrow(
            start_point=start.get_bottom(),
            end_point=end.get_top(),
            angle=angle,
        )
        end.set_parent_arrow(parent_arrow)
        return FadeIn(parent_arrow)

    def _calculate_position(self, level: int):
        parent = self.current_subproblem.parent
        if parent is None:
            return np.array([0, 3, 0])  # Root positioning in top center

        num_children_elements = len(self.elements) / ((self.subproblem_size) ** (level))
        self.subproblem_spacing = 6 / (level + 1) ** 1.1

        total_sibling_width = 0.8 * num_children_elements
        start_x = parent.get_center()[0] - total_sibling_width / 2
        x = start_x + (1.2 * self.subproblem_spacing * ((len(parent.children))) / 1.3)

        y = parent.get_center()[1] - self.level_spacing

        return np.array([x, y, 0])

    def traverse_up(self) -> AnimationGroup:
        """Emulates the upwards traversal of a recursive return statement. Use before returning in base case or inductive step."""
        # completed_animations = Wait(0.1)
        parent = self.current_subproblem.parent
        if parent:  # Could give to .set_parent_arrow or RecursiveArray class
            new_arrow = CurvedArrow(
                start_point=self.current_subproblem.get_top(),
                end_point=parent.get_bottom(),
                angle=0.0,
            )
            arrow_animation = self.current_subproblem.set_parent_arrow(new_arrow)
        else:
            arrow_animation = Wait(0.1)
        self.current_subproblem = parent
        return AnimationGroup(arrow_animation)

