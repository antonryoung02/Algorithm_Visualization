from Elements.Element import Element
from Elements.GraphElement import GraphElement
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Graph import Graph
from GraphIndicator import GraphIndicator

code = """

"""

# PYTHONPATH=$(pwd) manim -pql Implementations/TestGraph.py GraphScene
class GraphScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Circle:{"radius":0.5}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}
        self.indicator_style={Circle:{"radius":0.5, "color":"blue","stroke_width":10}, Text:{"font_size":30}}

    def construct(self):
        vals = [10, 15, 20, 6]
        e = [GraphElement(val, Circle(), self.element_style) for val in vals] 
        edges = [(e[0], e[1], 10), (e[1], e[2], 5), (e[0], e[3], 3), (e[1], e[0], 1), (e[2], e[3], 6)]
        positions = [[3,3,0], [1,1,0], [2,-3,0], [5,0,0]]
        graph = Graph(e, edges, positions)
        graph_indicator = GraphIndicator(graph, Circle(), self.indicator_style)
        self.play(graph.create())

        e.append(GraphElement(5, Circle(), self.element_style))
        self.play(graph.add_element(e[-1], [-2, 1,0]))
        self.play(graph.add_edge((e[-1], e[1], 0)))
        self.play(graph.add_edge((e[-1], e[2], 0)))
        self.play(graph_indicator.create(graph.elements[0]))
        for edge in graph.get_outgoing_edges_for_node(graph_indicator.current_node):
            self.play(graph_indicator.visit(edge[1]))
            self.play(graph_indicator.visit(edge[0]))


s = GraphScene()
s.construct()