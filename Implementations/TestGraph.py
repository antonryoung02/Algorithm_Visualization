from Elements.Element import Element
from Elements.GraphElement import GraphElement
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Graph import Graph
code = """

"""

# PYTHONPATH=$(pwd) manim -pql Implementations/TestGraph.py GraphScene
class GraphScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Circle:{"radius":0.5}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}

    def construct(self):
       vals = [10, 15, 20]
       e = [GraphElement(val, Circle(), self.element_style) for val in vals] 
       edges = [(e[0], e[1], 0), (e[1], e[2], 0), (e[1], e[0], 0)]
       positions = [[3,3,0], [1,1,0], [2,-3,0]]
       graph = Graph(e, edges, positions)
       self.play(graph.create())

       e.append(GraphElement(5, Circle(), self.element_style))
       self.play(graph.add_element(e[-1], [-2, 1,0]))
       self.play(graph.add_edge((e[-1], e[1], 0)))
       self.play(graph.add_edge((e[-1], e[2], 0)))
       


s = GraphScene()
s.construct()