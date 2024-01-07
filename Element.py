from manim import *

class Element(VGroup):
    def __init__(self, value, side_length=1.5, **kwargs):
        super().__init__(**kwargs)
        self.square = Square(side_length)
        self.text = Text(str(value))
        self.add(self.square, self.text)
