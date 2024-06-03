from manim import *
from Arrays.RecursiveArray import RecursiveArray

class Recursion(VGroup):
    def __init__(
        self,
        elements,
        positioner,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.elements = list(elements)
        self.positioner = positioner
        self.root = None
        self.current_subproblem = None

    def create(self) -> AnimationGroup:
        return self.divide_array(None, 0, 0, len(self.elements) - 1)

    def divide_array(
        self, parent: RecursiveArray, level: int, i: int, j: int
    ) -> AnimationGroup:
        """Recursive divide step, displaying new array made from array[i:j]"""
        if j - i < 0:
           return Wait(0.1)
        if level > 5:
            raise RecursionError(f"divide_array called too many times!")
        
        subproblem = RecursiveArray(self.elements[i:j+1], parent=parent)
        
        self.current_subproblem = subproblem
        self.current_subproblem.move_to(self.positioner.get_subproblem_position(self.current_subproblem))

        self.add(self.current_subproblem)

        if parent is not None:
            parent.children.append(self.current_subproblem)
            parent_arrow = CurvedArrow(start_point=parent.get_bottom(),end_point=self.current_subproblem.get_top(),angle=0)
            arrow_animation = self.current_subproblem.set_parent_arrow(parent_arrow)
        else:
            self.root = self.current_subproblem
            arrow_animation = Wait(0.1)

        return AnimationGroup(self.current_subproblem.create(), arrow_animation)

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

