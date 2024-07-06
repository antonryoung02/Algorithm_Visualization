from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
import random
code = """

"""
config.frame_size = (450,800) 
config.frame_width = 8
# PYTHONPATH=$(pwd) manim Implementations/Representations/OppositeEndTwoPointer.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.5}, Text:{"font_size":30}}
        self.font="Kanit"

    def construct(self):
        #Opposite ends tp
        heading = Text("'Opposite Ends' Two Pointer", font_size=40, font=self.font).to_corner(UP).shift(0.5*UP)
        title = Text("Two Integer Sum II", font_size=32, font=self.font).to_corner(UP).shift(3*DOWN)
        leetnum = Text("(Leetcode #167)", font_size=32, font=self.font).move_to(title).shift(0.5*DOWN)
        desc = Text("Given a sorted array find the indices of", font_size=24, font=self.font).move_to(leetnum).shift(0.75*DOWN)
        desc2 = Text("two integers that add up to a target value", font_size=24, font=self.font).move_to(desc).shift(0.5* DOWN)
        array, lp, rp = self.create_array_lp_rp()
        i = 1; j = len(array)-2
        self.play(FadeIn(heading), FadeIn(leetnum), FadeIn(desc), FadeIn(desc2), FadeIn(title), array.create(), lp.create(0), rp.create(len(array)-1))
        while i <= j:
            self.play(lp.update(i), rp.update(j))
            i += 1
            j -= 1
        self.play(array.delete(), lp.delete(), rp.delete(), FadeOut(heading), FadeOut(leetnum), FadeOut(desc), FadeOut(desc2), FadeOut(title))

    def create_array_lp_rp(self):
        elements = [Element("", Square(), self.element_style) for i in range(12)]
        array = Array(elements).to_corner(UP).shift(3*LEFT).shift(DOWN)
        lp = Pointer(array, UP, style={"color":"red"})
        rp = Pointer(array, UP, style={"color":"blue"})
        return array, lp, rp



s = MyScene()
s.construct()