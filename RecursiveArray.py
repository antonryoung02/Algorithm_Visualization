from manim import *
from Array import Array

class RecursiveArray(Array):
    def __init__(self, values, side_length=1.5, gap=0.0, parent=None, **kwargs):
        super().__init__(values, side_length, gap, **kwargs)
        
        self.parent = parent
        self.children = []
        self.parent_arrow = None
    
    def set_parent_arrow(self, parent_arrow):
        prev_arrow = self.parent_arrow
        self.parent_arrow = parent_arrow

        if prev_arrow is None:
            return FadeIn(self.parent_arrow)
        else:
            return [Transform(prev_arrow, self.parent_arrow)]


