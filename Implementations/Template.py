from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion

code = """

"""

# PYTHONPATH=$(pwd) manim -pql Implementations/MergeSort.py MergesortScene
class TemplateScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":1}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}

    def construct(self):
        lp = Pointer(None, UP, style={"color":"red"}, name="i")
        pass

s = TemplateScene()
s.construct()