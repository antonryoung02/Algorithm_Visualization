from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Windows.CodeWindow import CodeWindow

code = """
class Solution:
    def moveZeroes(self, nums):
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
"""
config.frame_size = (450,800) 
config.frame_width = 8
# PYTHONPATH=$(pwd) manim -pql Implementations/MoveZeroes_283.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.9}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3.5, "height":0.9}, Text:{"font_size":30}}
        self.font="Kanit"

    def construct(self):
        nums = [0, 3, 0, 16, 1, 0, 10, 4] 
        elements = [Element(n, Square(), self.element_style) for n in nums]
        code_window = CodeWindow(code).scale(1.6)
        code_window.to_corner(DOWN).shift(1.5*DOWN)

        array = Array(elements)        
        array.to_corner(UP).shift(3.1*LEFT).shift(UP)

        ip = Pointer(array, UP, style={"color": "red"}, name="lp")
        jp = Pointer(array, UP, style={"color": "blue"}, name="rp")
        i = 0
        j = 0

        self.play(array.create(), jp.create(0), ip.create(), code_window.create(), code_window.animate.set_opacity(1))
        self.play(code_window.highlight([3,4]))

        while j < len(nums):
            if nums[j] == 0:
                self.play(code_window.highlight([5,6]))
                j += 1
                self.play(code_window.highlight(7), jp.update(j))
            else:
                nums[i] = nums[j]
                self.play(code_window.highlight([5,8]))
                self.play(code_window.highlight(9), array.elements[i].set_data(nums[j]))
                i += 1
                j += 1
                self.play(code_window.highlight([10,11]), ip.update(i), jp.update(j))
        self.play(jp.delete())
        while i < len(nums):
            nums[i] = 0
            self.play(code_window.highlight(13), array.elements[i].set_data(0))
            i += 1
            self.play(code_window.highlight(14), ip.update(i))
        self.play(ip.delete())
            

scene = MyScene()
scene.construct()
