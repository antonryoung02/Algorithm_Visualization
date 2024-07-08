from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import *
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Windows.CodeWindow import CodeWindow

code = """
class Solution(object): 
    def maxProfit(self, prices):
        i = 0
        j = 0
        max_profit = 0
        while j < len(prices):
            current_profit = prices[j] - prices[i]
            max_profit = max(max_profit, current_profit)
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                j += 1
        return max_profit
"""
config.frame_size = (450,800) 
config.frame_width = 8
# PYTHONPATH=$(pwd) manim Implementations/BuySellStock_121.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.9}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":30}}
        self.font="Kanit"

    def construct(self):
        prices = [5, 12, 3, 1, 6, 5, 9, 7] 
        elements = [Element(p, Square(), self.element_style) for p in prices]
        code_window = CodeWindow(code, scale_bg_height=1.7).scale(1.3)
        code_window.to_corner(DOWN).shift(2.3*DOWN)

        array = Array(elements)        
        array.to_corner(UP).shift(3.1*LEFT).shift(UP)

        ip = Pointer(array, UP, style={"color": "red"}, name="i")
        jp = Pointer(array, UP, style={"color": "blue"}, name="j")
        window_arr = Array([Element(0, Rectangle(), self.window_element_style), Element(0, Rectangle(), self.window_element_style)])
        window_arr.move_to(array).shift(2.5*DOWN)
        curr_prof_text = Text("curr_profit", font=self.font, font_size=24).next_to(window_arr[0], DOWN)
        max_prof_text = Text("max_profit", font=self.font, font_size=24).next_to(window_arr[1], DOWN)


        self.play(FadeIn(curr_prof_text), FadeIn(max_prof_text), code_window.create(), window_arr.create(), array.create(), code_window.animate.set_opacity(1))

        i = 0
        j = 0
        max_profit = 0
        self.play(ip.create(), jp.create(), code_window.highlight([3,4,5]))

        while j < len(prices):
            curr_profit = prices[j] - prices[i]
            max_profit = max(max_profit, curr_profit)

            self.play(code_window.highlight([6,7]), self.a.move_element_data_to_other(array.elements[i], window_arr[0]), 
                        self.a.move_element_data_to_other(array.elements[j], window_arr[0]),
                        self.a.show_math_then_set_data(window_arr[0], f"{prices[j]} - {prices[i]}", curr_profit))

            self.play(self.a.compare_size(window_arr.elements[0], window_arr.elements[1]))
            if max_profit == curr_profit:
                self.play(code_window.highlight(8), window_arr[1].set_data(curr_profit))
            else:
                self.play(code_window.highlight(8))

            if prices[j] < prices[i]:
                self.play(code_window.highlight([9,10,11]), ip.update(j), jp.update(j+1))
                i = j
                j += 1
            else:
                self.play(code_window.highlight([12, 13]), jp.update(j+1))
                j += 1

        self.play(code_window.highlight(14))
        return max_profit

s = MyScene()
s.construct()