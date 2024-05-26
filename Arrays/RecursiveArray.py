from manim import *
from Arrays.Array import Array


class RecursiveArray(Array):
    """Array with added attributes for navigating through recursion tree"""

    def __init__(self, elements, parent=None, **kwargs):
        super().__init__(
            elements,
            **kwargs
        )
        self.parent = parent
        self.children = []
        self.parent_arrow = None

    def set_parent_arrow(self, parent_arrow):
        prev_arrow = self.parent_arrow
        self.parent_arrow = parent_arrow

        if prev_arrow is None:
            return FadeIn(self.parent_arrow)
        return Transform(prev_arrow, self.parent_arrow)

    def clear_array(self):
        return AnimationGroup(*[element.set_data("_") for element in self.elements])