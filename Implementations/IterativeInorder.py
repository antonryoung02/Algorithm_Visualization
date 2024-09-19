from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Utils.TreeDS import *
from Recursion.BinaryTree import BinaryTree
from Recursion.PositionStrategies import BinaryTreePositioner
from Elements.TreeElement import TreeElement
from TreeIndicator import Indicator 
code = """

"""

# PYTHONPATH=$(pwd) manim -pql Implementations/IterativeInorder.py IterativeInorderScene
class IterativeInorderScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Circle:{"radius":0.5}, Text:{"font_size":30}}
        self.indicator_style={Circle:{"radius":0.6, "color":BLUE}, Text:{"font_size":30}}
        self.visited_style={Circle:{"radius":0.5, "color":GREEN}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}

    def construct(self):
        array_data = [1,2,3,4,5,8,6,7,9]
        root = binary_tree_from_list(array_data)
        
        elements = [TreeElement(i, shape=Circle(), style=self.element_style) for i in array_data]
        positioner = BinaryTreePositioner(vertical_spacing=1.5)
        tree = BinaryTree(elements, positioner)
        curr = Indicator(tree, Circle(), self.indicator_style)
        
        curr.set_current_node(root)
        self.play(tree.create(), curr.create())
        
        q = []
        visited = []
        while root or q:
            while root:
                q.append(root)
                root = root.left
                self.play(curr.go_left())
            root = q.pop()
            self.play(curr.set_current_node(root), tree.current_node.set_style(self.visited_style))
            visited.append(root)
            self.play(curr.go_right())
            root = root.right
        return visited
            

s = IterativeInorderScene()
s.construct()