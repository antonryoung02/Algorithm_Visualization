from Elements.Element import Element
from Elements.TreeElement import TreeElement
from manim import * 
# PYTHONPATH=$(pwd) manim -pql Elements/TestElement.py ElementTestScene
class ElementTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        e = TreeElement({"val1": "5", "val2":"10"}, {"font_size":20})
        self.play(e.create())
        self.wait(1)
        self.play(e.set_data({"val1": "6", "val2":"2"}))
        self.wait(1)
        self.play(e.set_style({"width":2, "height":1, "color":"red", "font_size":20}))
        self.wait(1)
        self.play(e.delete())
        self.wait(1)

