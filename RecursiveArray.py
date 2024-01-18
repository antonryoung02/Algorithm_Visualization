from manim import *
from Array import Array


class RecursiveArray(Array):
    """Array with added attributes for navigating through recursion tree"""

    def __init__(self, scene, values, side_length=1.5, gap=0.0, parent=None, **kwargs):
        super().__init__(
            scene,
            values,
            side_length=side_length,
            gap=gap,
            stack_direction=RIGHT,
            **kwargs
        )

        self.parent = parent
        self.children = []
        self.parent_arrow = None

    def set_parent(self, new_parent):
        self.parent = new_parent

    def set_parent_arrow(self, parent_arrow):
        prev_arrow = self.parent_arrow
        self.parent_arrow = parent_arrow

        if prev_arrow is None:
            return FadeIn(self.parent_arrow)
        return Transform(prev_arrow, self.parent_arrow)

    def show_completed(self):
        color_animations = []
        for element in self.elements:
            color_animations.append(FadeToColor(element.square, "#00FF00"))

        return AnimationGroup(*color_animations)
