from manim import *
from enum import Enum
from enum import auto


class Element(VGroup):
    def __init__(self, value, side_length=1.5, **kwargs):
        super().__init__(**kwargs)
        self.square = Square(side_length)
        self.text = Text(str(value))
        self.value = value
        self.add(self.square, self.text)

    def set_value(self, new_val):
        self.value = new_val
        self.remove(self.text)
        self.text = Text(str(new_val))
        self.text.move_to(self.square)
        self.add(self.text)
        return ReplacementTransform(self.text, self.text)
