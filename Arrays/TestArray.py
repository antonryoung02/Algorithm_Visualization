from Elements.Element import Element
from Elements.TreeElement import TreeElement
from Arrays.Array import Array
from manim import * 
# PYTHONPATH=$(pwd) manim -pql Arrays/TestArray.py ArrayTestScene
class ArrayTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        elements = [Element(str(i), {"side_length":1}) for i in range(3)]
        array = Array(elements)
        self.add(array)
        self.play(array.create())
        self.wait(1)
        self.play(array.change_element(1, data="20"))
        self.wait(1)
        self.play(array.remove_element(0))
        # self.play(e.set_data({"val1": "6", "val2":"2"}))
        self.wait(1)
        self.play(array.change_element(2, data="12"))
        self.wait(1)
        self.play(array.insert_element(1, Element("23", {"side_length":1})))
        self.wait(1)
        self.play(array.remove_element(1))
        self.wait(1)
        self.play(array.delete())
        self.wait(1)

ats = ArrayTestScene()
ats.construct()