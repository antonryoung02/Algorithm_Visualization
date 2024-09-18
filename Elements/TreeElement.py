from Elements.Element import Element
from manim import *

class TreeNode(Element):
    def __init__(self, data, shape=Circle(), style={Circle:{}, Text:{}}, callbacks=[], **kwargs):
        super().__init__(data, shape, style, callbacks, **kwargs)
        self.parent = None
        self.parent_arrow = None
        self.left_child = None
        self.right_child = None

    def create(self):
        if self.parent_arrow is not None:
            return AnimationGroup(FadeIn(self.parent_arrow), FadeIn(self.shape), FadeIn(self.data))
        return AnimationGroup(FadeIn(self.shape), FadeIn(self.data)) 

    def set_left_child(self, new_child):
        self.left_child = new_child
        new_child.parent = self

    def set_parent_arrow(self, parent_arrow):
        prev_arrow = self.parent_arrow
        self.parent_arrow = parent_arrow

        if prev_arrow is None:
            return FadeIn(self.parent_arrow)
        return Transform(prev_arrow, self.parent_arrow)

    def set_right_child(self, new_child):
        self.right_child = new_child
        new_child.parent = self
        new_child.parent_arrow = CurvedArrow(self.get_bottom(), new_child.get_top())
