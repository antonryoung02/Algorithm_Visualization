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
    def twoSum(self, numbers, target):
        lp = 0
        rp = len(numbers) - 1
        while lp < rp:
            curr_sum = numbers[lp] + numbers[rp]
            if curr_sum > target:
                rp -= 1
            elif curr_sum < target:
                lp += 1
            else:
                break
        return [lp + 1, rp + 1]
"""
config.frame_size = (450,800) 
config.frame_width = 8
# PYTHONPATH=$(pwd) manim -pql Implementations/TwoSum_167.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.9}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3.5, "height":0.9}, Text:{"font_size":30}}
        self.font="Kanit"

    def construct(self):
        numbers = [5, 3, 20, 6, 7, 13, 10, 1] 
        target = 12
        elements = [Element(n, Square(), self.element_style) for n in numbers]
        code_window = CodeWindow(code).scale(1.4)
        code_window.to_corner(DOWN).shift(2*DOWN)

        array = Array(elements)        
        array.to_corner(UP).shift(3.1*LEFT).shift(UP)


        target_element = Element(target, Rectangle(), self.window_element_style)
        curr_sum_element = Element(0, Rectangle(), self.window_element_style)
        window_arr = Array([curr_sum_element, target_element]).move_to(array).shift(2.5*DOWN)
        target_text = Text("target", font=self.font, font_size=24).next_to(window_arr[1], DOWN)
        curr_sum_text = Text("curr_sum", font=self.font, font_size=24).next_to(window_arr[0], DOWN)

        ip = Pointer(array, UP, style={"color": "red"}, name="lp")
        jp = Pointer(array, UP, style={"color": "blue"}, name="rp")
        i = 0
        j = len(numbers) - 1

        self.play(FadeIn(target_text), FadeIn(curr_sum_text), window_arr.create(), array.create(), jp.create(len(array)-1), ip.create(), code_window.create(), code_window.animate.set_opacity(1))

        numbers = sorted(numbers)
        self.play(self.a.sort(array))

        while i < j:
            curr_sum = numbers[i] + numbers[j]
            self.play(self.a.move_element_data_to_other(array.elements[i], window_arr[0]), self.a.move_element_data_to_other(array.elements[j], window_arr[0]), window_arr[0].set_data(curr_sum), code_window.highlight(6))
            if curr_sum > target:
                self.play(code_window.highlight(7), self.a.compare_size(0, 1, window_arr))
                j -= 1
                self.play(code_window.highlight(8), jp.update(j))
            elif curr_sum < target:
                self.play(code_window.highlight(9), self.a.compare_size(0, 1, window_arr))
                i += 1
                self.play(code_window.highlight(10), ip.update(i))
            else:
                self.play(code_window.highlight(11))
                self.play(code_window.highlight(12))
                break

        self.play(code_window.highlight(13))
        return [i + 1, j + 1]

scene = MyScene()
scene.construct()
