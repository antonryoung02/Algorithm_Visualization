from manim import *
from Arrays.RecursiveArray import RecursiveArray

class Recursion(VGroup):
    def __init__(
        self,
        elements,
        positioner,
        callbacks=[],
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.elements = list(elements)
        self.callbacks = callbacks
        self.positioner = positioner
        self.root = None
        self.current_subproblem = None

    def create(self) -> AnimationGroup | None:
        return self.divide_array(None, 0, 0, len(self.elements) - 1)

    def divide_array(
        self, parent: RecursiveArray | None, level: int, i: int, j: int
    ) -> AnimationGroup | None:
        """Recursive divide step, displaying new array made from array[i:j]"""
        if j - i < 0:
           return AnimationGroup(Wait(0.1))
        if level > 5:
            raise RecursionError("divide_array probably called too many times!")

        visit_end_animations = Wait(0) 
        if self.current_subproblem:
            visit_end_animations = self.call_callback_hooks("on_visit_end") 
        
        self.current_subproblem = RecursiveArray(self.elements[i:j+1], parent=parent)
        self.current_subproblem.move_to(self.positioner.get_subproblem_position(self.current_subproblem))
        self.add(self.current_subproblem)

        visit_start_animations = self.call_callback_hooks("on_visit_start")

        if parent:
            parent.children.append(self.current_subproblem)
            parent_arrow = CurvedArrow(start_point=parent.get_bottom(),end_point=self.current_subproblem.get_top(),angle=0)
            arrow_animation = self.current_subproblem.set_parent_arrow(parent_arrow)
        else:
            self.root = self.current_subproblem
            arrow_animation = Wait(0)

        return Succession(visit_end_animations, 
                          AnimationGroup(self.current_subproblem.create(), visit_start_animations, arrow_animation), 
                          visit_start_animations)

    def traverse_up(self) -> AnimationGroup | None:
        """Emulates the upwards traversal of a recursive return statement. Use before returning in base case or inductive step."""
        visit_end_animations = self.call_callback_hooks("on_visit_end")
        parent = self.current_subproblem.parent
        if parent:  # Could give to .set_parent_arrow or RecursiveArray class
            new_arrow = CurvedArrow(
                start_point=self.current_subproblem.get_top(),
                end_point=parent.get_bottom(),
                angle=0.0,
            )
            arrow_animation = self.current_subproblem.set_parent_arrow(new_arrow)
        else:
            arrow_animation = Wait(0)
        self.current_subproblem = parent
        visit_start_animations = self.call_callback_hooks("on_visit_start")
        return Succession(visit_end_animations, AnimationGroup(arrow_animation), visit_start_animations)
    
    def replace_current_subproblem(self, new_elements):
        old_subproblem_animation = FadeOut(self.current_subproblem)
        new_subproblem = RecursiveArray(new_elements, parent=self.current_subproblem.parent)
        new_subproblem.move_to(self.current_subproblem.get_center())
        
        if self.current_subproblem.parent is not None:
            subproblem_index = self.current_subproblem.parent.children.index(self.current_subproblem)
            self.current_subproblem.parent.children[subproblem_index] = new_subproblem
            new_subproblem.set_parent_arrow(self.current_subproblem.parent_arrow)
        self.current_subproblem = new_subproblem
        
        return AnimationGroup(old_subproblem_animation, FadeIn(new_subproblem))
        
    
    def call_callback_hooks(self, method_name):
        animations = []
        for callback in self.callbacks:
            method = getattr(callback, method_name, None)
            if callable(method):
                animations.append(method(self))
            else:
                print(f"Warning: '{method_name}' method not found in {callback}")
        return AnimationGroup(*animations)

