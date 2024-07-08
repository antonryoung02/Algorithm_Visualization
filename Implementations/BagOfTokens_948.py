from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Windows.CodeWindow import CodeWindow
from Callbacks.ElementCallbacks import ShowVisitCompleteElementCallback

code = """
class Solution:
    def bagOfTokensScore(self, tokens, power):
        score = 0
        lp = 0
        rp = len(tokens) - 1
        max_score = 0
        tokens.sort()
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
        elements = [Element(n, Square(), self.element_style, callbacks=[]) for n in numbers]
        code_window = CodeWindow(code).scale(1.2)
        code_window.to_corner(DOWN).shift(3*DOWN)

        array = Array(elements)        
        array.to_corner(UP).shift(3.1*LEFT).shift(UP)

        power = 12

        score_element = Element("0", Rectangle(), self.window_element_style)
        max_score_element = Element("0", Rectangle(), self.window_element_style) 
        power_element = Element(str(power), Rectangle(), self.window_element_style)
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
        self.play(code_window.highlight([3,4,5,6]))   
        numbers = sorted(numbers)
        self.play(code_window.highlight(7), self.a.sort(array))
        ip.current_element = array.elements[0]
        jp.current_element = array.elements[len(array)-1]

        while i <= j:
            if power >= numbers[i]:
                self.play(code_window.highlight([8,9]))
                power -= numbers[i]
                i += 1
                score += 1
                self.play(code_window.highlight([10,11,12]), 
                          self.a.move_element_data_to_other(array.elements[i-1], window_arr[0], RED), 
                          window_arr[1].set_data(str(score)),
                          ip.update(i), 
                          self.a.show_math_then_set_data(window_arr[0], f"{window_arr[0].get_data()}-{numbers[i-1]}", str(power)),
                          )
                
                max_score = max(max_score, score)
                self.play(code_window.highlight(13), window_arr[2].set_data(str(max_score)))
            elif score > 0:
                self.play(code_window.highlight([8, 14]))
                power += numbers[j]
                j -= 1
                score -= 1
                self.play(code_window.highlight([15,16,17]),
                          window_arr[1].set_data(str(score)),
                          jp.update(j),
                          self.a.move_element_data_to_other(array.elements[j+1], window_arr[0], GREEN), 
                          self.a.show_math_then_set_data(window_arr[0], f"{window_arr[0].get_data()}+{numbers[j+1]}", str(power)),)
            else:
                self.play(code_window.highlight([18,19]))
                break

        self.play(code_window.highlight(20))
        return max_score

scene = MyScene()
scene.construct()
