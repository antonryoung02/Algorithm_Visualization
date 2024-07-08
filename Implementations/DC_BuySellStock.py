from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import *
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Windows.CodeWindow import CodeWindow
from Recursion.PositionStrategies import TwoChildrenPositioner
from Callbacks.ElementCallbacks import displayCodeRecursionCallback, zoomToElementCallback, zoomToRecursionCallback
code = """
class Solution(object):
    def maxProfit(self, prices):
        profit, _, _ = self.maxProfHelper(prices, 0, len(prices)-1)
        return profit
    
    def maxProfHelper(self, prices, i, j):
        if i == j:
            return 0, prices[i], prices[i]
        
        midpt = (i + j) // 2
        l_profit, l_min, l_max = self.maxProfHelper(prices, i, midpt)
        r_profit, r_min, r_max = self.maxProfHelper(prices, midpt + 1, j)

        max_prof = max(l_profit, r_profit, r_max - l_min)
        min_val = min(r_min, l_min)
        max_val = max(r_max, l_max)
        return max_prof, min_val, max_val
"""
# config.frame_size = (450,800) 
# config.frame_width = 8
# PYTHONPATH=$(pwd) manim Implementations/DC_BuySellStock.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":1}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":1.6, "height":1}, Text:{"font_size":20}}
        self.code_window = CodeWindow(code, scale_bg_height=1.8).set_opacity(0).scale(0.9)

    def construct(self):
        data = [5, 12, 3, 1, 6, 5, 9, 7] 
        elements = [Element(i, Square(), self.element_style, []) for i in data]
        recursion_positioner = TwoChildrenPositioner(1.6, 0.9)
        # recursion_callback = displayCodeRecursionCallback(self.code_window, [1, 7, 13], LEFT)
        # recursion_zoom_callback = zoomToRecursionCallback(self, [1,7,13], 16)
        r = Recursion(elements, recursion_positioner)
        self.play(r.create(), self.code_window.create())
        self.recursion(r, data, 0, len(data)-1, 0)

    def recursion(self, array, data, i, j, level):
        if j - i <= 0:
            self.play(array.replace_current_subproblem([Element({"max_profit":0, "min_val":data[i], "max_val":data[i]}, Rectangle(), self.window_element_style)]))
            self.play(self.a.show_completed(array.current_subproblem), array.traverse_up())
            return 0, data[i], data[i]
        
        midpt = (i + j) // 2
        self.play(array.divide_array(array.current_subproblem, level, i, midpt))
        left_profit, left_min, left_max = self.recursion(array, data, i, midpt, level + 1)

        self.play(array.divide_array(array.current_subproblem, level, midpt+1, j))
        right_profit, right_min, right_max = self.recursion(array, data, midpt+1, j, level + 1)

        max_prof = max(left_profit, right_profit, right_max - left_min)
        min_val = min(right_min, left_min)
        max_val = max(right_max, left_max)
        
        self.play(array.replace_current_subproblem([Element({"max_profit":max_prof, "min_val":min_val, "max_val":max_val}, Rectangle(), self.window_element_style)]))
        self.play(self.a.show_completed(array.current_subproblem), array.traverse_up())
        return max_prof, min_val, max_val



s = MyScene()
s.construct()