from manim import *
from Elements.TreeElement import TreeElement


# __init__(self, data: dict, parent=None, side_width=4, side_height=3, **kwargs):
class VariableWindow(TreeElement):
    def __init__(self, data=None, style=None, **kwargs):
        super().__init__(data, style, **kwargs) 
