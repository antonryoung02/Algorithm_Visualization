from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
import random
code = """

"""

# PYTHONPATH=$(pwd) manim Implementations/Representations/OppositeEndTwoPointer.py MyScene
class MyScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.5}, Text:{"font_size":30}}

    def construct(self):
        #Opposite ends tp
        array, lp, rp = self.create_array_lp_rp()
        i = 1; j = len(array)-2
        self.play(array.create(), lp.create(0), rp.create(len(array)-1))
        while i <= j:
            self.play(lp.update(i), rp.update(j))
            i += 1
            j -= 1
        self.play(array.delete(), lp.delete(), rp.delete())

        #1-State tp
        array, lp, rp = self.create_array_lp_rp()
        i = 0
        self.play(array.create(), lp.create(0), rp.create(0))
        while i < len(array):
            k = i
            for _ in range(random.randint(2, 4)):
                k += 1
                self.play(rp.update(k))
            i += 1
            self.play(lp.update(i), rp.update(i))
        self.play(array.delete(), lp.delete(), rp.delete())

        #Fixed slid wind
        array, lp, rp = self.create_array_lp_rp()
        i = 0; j = 3
        self.play(array.create(), lp.create(0), rp.create(j))
        while j < len(array):
            self.play(lp.update(i), rp.update(j))
            i += 1
            j += 1
        self.play(array.delete(), lp.delete(), rp.delete())

        #Var slid wind
        array, lp, rp = self.create_array_lp_rp()
        i = 0; j = 3
        self.play(array.create(), lp.create(0), rp.create(j))
        while j < len(array) and i < len(array):
            if i < j and random.random() > 0.5:
                i += 1
                self.play(lp.update(i))
            else:
                j += 1
                self.play(rp.update(j))
        self.play(array.delete(), lp.delete(), rp.delete())




    def create_array_lp_rp(self):
        elements = [Element("", Square(), self.element_style) for i in range(12)]
        array = Array(elements)
        lp = Pointer(array, UP, style={"color":"red"})
        rp = Pointer(array, UP, style={"color":"blue"})
        return array, lp, rp



s = MyScene()
s.construct()