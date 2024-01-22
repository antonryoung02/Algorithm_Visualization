from manim import *
from TreeElement import TreeElement


# __init__(self, data: dict, parent=None, side_width=4, side_height=3, **kwargs):
class VariableWindow(TreeElement):
    def __init__(self, data={}, font_size=30):
        super().__init__(
            data, side_width=3, side_height=3, font_size=font_size
        )  # Make it larger
