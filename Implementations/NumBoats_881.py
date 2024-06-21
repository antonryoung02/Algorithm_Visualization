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
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        num_boats = 0
        lp = 0
        rp = len(people) - 1
        while lp <= rp:
            person_sum = people[lp] + people[rp]
            if person_sum <= limit:
                lp += 1
                rp -= 1
            else:
                rp -= 1
            num_boats += 1
        return num_boats
"""
config.frame_size = (450,800) 
config.frame_width = 8
# PYTHONPATH=$(pwd) manim -pql Implementations/NumBoats_881.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.9}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":2.5, "height":0.9}, Text:{"font_size":30}}
        self.font="Kanit"

    def construct(self):
        numbers = [1, 9, 3, 2, 5, 1, 4, 7]
        limit = 9
        elements = [Element(n, Square(), self.element_style) for n in numbers]
        code_window = CodeWindow(code).scale(1.3)
        code_window.to_corner(DOWN).shift(2*DOWN)

        array = Array(elements)        
        array.to_corner(UP).shift(3.1*LEFT).shift(UP)

        limit_element = Element(limit, Rectangle(), self.window_element_style)
        person_sum_element = Element(0, Rectangle(), self.window_element_style)
        num_boats_element = Element(0, Rectangle(), self.window_element_style)
        window_arr = Array([person_sum_element, limit_element, num_boats_element]).move_to(array).shift(2.5*DOWN)
        target_text = Text("limit", font=self.font, font_size=24).next_to(window_arr[1], DOWN)
        curr_sum_text = Text("person_sum", font=self.font, font_size=24).next_to(window_arr[0], DOWN)
        num_boats_text = Text("num_boats", font=self.font, font_size=24).next_to(window_arr[2], DOWN)

        ip = Pointer(array, UP, style={"color": "red"}, name="lp")
        jp = Pointer(array, UP, style={"color": "blue"}, name="rp")
        i = 0
        j = len(numbers) - 1
        num_boats = 0

        self.play(FadeIn(num_boats_text), FadeIn(target_text), FadeIn(curr_sum_text), window_arr.create(), array.create(), jp.create(len(array)-1), ip.create(), code_window.create(), code_window.animate.set_opacity(1))

        numbers = sorted(numbers)
        self.play(self.a.sort(array))

        while i <= j:
            person_sum = numbers[i] + numbers[j]
            self.play(self.a.move_element_data_to_other(array.elements[i], window_arr[0]), self.a.move_element_data_to_other(array.elements[j], window_arr[0]), window_arr[0].set_data(person_sum))
            if person_sum <= limit:
                self.play(self.a.compare_size(0, 1, window_arr))
                i += 1
                j -= 1
                self.play(jp.update(j), ip.update(i))
            else:
                j -= 1
                self.play(jp.update(j))
            num_boats += 1
            self.play(window_arr[2].set_data(num_boats))

        return num_boats

scene = MyScene()
scene.construct()
