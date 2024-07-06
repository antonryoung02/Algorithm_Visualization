from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
# PYTHONPATH=$(pwd) manim -pql Arrays/TestArray.py ArrayTestScene
class ArrayTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        pass

ats = ArrayTestScene()
ats.construct()