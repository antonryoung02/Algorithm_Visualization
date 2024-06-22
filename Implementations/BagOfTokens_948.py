from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Windows.CodeWindow import CodeWindow

code = """
class Solution:
    def bagOfTokensScore(self, tokens, power):
        score = 0
        lp = 0
        rp = len(tokens) - 1
        max_score = 0
        tokens = sorted(tokens)
        
        while lp <= rp:
            if power >= tokens[lp]:
                power -= tokens[lp]
                lp += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[rp]
                rp -= 1
                score -= 1
            else:
                break
        return max_score

"""
config.frame_size = (450,800) 
config.frame_width = 8
# PYTHONPATH=$(pwd) manim -pql Implementations/BagOfTokens_948.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.9}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":2.5, "height":0.9}, Text:{"font_size":30}}
        self.font="Kanit"

    def construct(self):
        numbers = [5, 7, 20, 6, 7, 13, 10, 12] 
        elements = [Element(n, Square(), self.element_style) for n in numbers]
        code_window = CodeWindow(code).scale(1.2)
        code_window.to_corner(DOWN).shift(3*DOWN)

        array = Array(elements)        
        array.to_corner(UP).shift(3.1*LEFT).shift(UP)

        power = 12

        score_element = Element(0, Rectangle(), self.window_element_style)
        max_score_element = Element(0, Rectangle(), self.window_element_style) 
        power_element = Element(power, Rectangle(), self.window_element_style)
        window_arr = Array([power_element, score_element, max_score_element]).move_to(array).shift(2.2*DOWN)
        score_text = Text("score", font=self.font, font_size=24).next_to(window_arr[1], DOWN)
        max_score_text = Text("max_score", font=self.font, font_size=24).next_to(window_arr[2], DOWN)
        power_text = Text("power", font=self.font, font_size=24).next_to(window_arr[0], DOWN) 

        ip = Pointer(array, UP, style={"color": "red"}, name="lp")
        jp = Pointer(array, UP, style={"color": "blue"}, name="rp")
        i = 0
        j = len(numbers) - 1
        score = 0
        max_score = 0

        self.play(FadeIn(score_text), FadeIn(max_score_text), FadeIn(power_text), window_arr.create(), 
                  array.create(), jp.create(len(array)-1), ip.create(), code_window.create(), code_window.animate.set_opacity(1))   
        self.play(code_window.highlight([3,4,5,6]) )   
        numbers = sorted(numbers)
        self.play(code_window.highlight(7), self.a.sort(array))

        while i <= j:
            if power >= numbers[i]:
                self.play(code_window.highlight(10))
                power -= numbers[i]
                i += 1
                score += 1
                self.play(code_window.highlight([11,12,13]), self.a.check_size(0, 1000, window_arr), self.a.check_size(1, -1000, window_arr),
                          self.a.move_element_data_to_other(array[i], window_arr[0]), window_arr[1].set_data(score), 
                          ip.update(i), window_arr[0].set_data(power))
                max_score = max(max_score, score)
                self.play(code_window.highlight(14), window_arr[2].set_data(max_score))
            elif score > 0:
                self.play(code_window.highlight(15))
                power += numbers[j]
                j -= 1
                score -= 1
                self.play(code_window.highlight([16,17,18]), self.a.check_size(0, -1000, window_arr), self.a.check_size(1, 1000, window_arr) ,
                          window_arr[1].set_data(score), jp.update(j), 
                          self.a.move_element_data_to_other(array[j], window_arr[0]), window_arr[0].set_data(power))
            else:
                self.play(code_window.highlight([19, 20]))
                break

        self.play(code_window.highlight(21))
        return max_score

scene = MyScene()
scene.construct()