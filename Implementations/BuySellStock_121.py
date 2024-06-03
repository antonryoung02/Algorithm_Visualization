from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import *
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Windows.CodeWindow import CodeWindow

code = """
class Solution(object): 
    def maxProfit(self, prices):
        i = 0; j = 0
        max_profit = 0
        while j < len(prices):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i = j
            j += 1
        return max_profit
"""

class BuySellStock_121(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator()
        self.element_style={Square:{"side_length":1}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}


    def construct(self):
        prices = [3, 8, 1, 4, 16, 5, 9, 7] 
        elements = [Element(p, Square(), self.element_style) for p in prices]
        code_window = CodeWindow(code)
        code_window.to_corner(UP+RIGHT)

        array = Array(elements)        
        array.to_corner(UP+LEFT).shift(DOWN)
        title = Text("Best Time to Buy and Sell Stock", font_size=40).to_corner(UP+LEFT)

        ip = Pointer(array, UP, style={"color": "red"}, name="i")
        jp = Pointer(array, UP, style={"color": "blue"}, name="j")
        window = Array([Element({"max_profit":0}, Rectangle(), self.window_element_style)])
        window.to_corner(DOWN + LEFT)

        self.play(code_window.create(), window.create(), array.create(), FadeIn(title))

        i = 0
        j = 0
        self.play(ip.create(), jp.create(), code_window.highlight(3))

        max_profit = 0
        self.play(code_window.highlight(4))

        while j < len(prices):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
                self.play(self.a.indicate(0, window), self.a.indicate(i, array), self.a.indicate(j, array), window[0].set_data({"max_profit":max_profit}), code_window.highlight(7))

            if prices[j] < prices[i]:
                self.play(ip.update(j), self.a.compare_size(j, i, array), code_window.highlight(9))
                i = j
            else:
                self.play(self.a.compare_size(j, i, array))
            j += 1
            self.play(jp.update(j), code_window.highlight(10))
        self.play(code_window.highlight(11), self.a.indicate(0, window))
        return max_profit

bss = BuySellStock_121()
bss.construct()