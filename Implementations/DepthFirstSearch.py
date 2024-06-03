from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Recursion.BinaryTree import BinaryTree
from Elements.TreeNode import TreeNode
from Recursion.PositionStrategies import BinaryTreePositioner
code = """

"""

# PYTHONPATH=$(pwd) manim -pql Implementations/DepthFirstSearch.py DFSScene
class DFSScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator()
        self.element_style={Circle:{"radius":0.5}, Text:{"font_size":30}}
        self.visited_style={Circle:{"radius":0.5, "color":GREEN}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}

    def construct(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8,9, 10, None]; elements = []
        for v in values:
            if v is None:
                elements.append(None)
            else:
                elements.append(TreeNode(v, Circle(), self.element_style))
        positioner = BinaryTreePositioner(1.5, 4)
        tree = BinaryTree(elements, positioner)
        self.play(tree.create(), tree.current_node.set_style(self.visited_style))
        self.play(tree.go_left(), tree.current_node.set_style(self.visited_style))
        self.play(tree.go_left(), tree.current_node.set_style(self.visited_style))
        self.play(tree.go_right(), tree.current_node.set_style(self.visited_style))
        self.play(tree.go_up(), tree.current_node.set_style(self.visited_style))
        self.play(tree.insert(TreeNode(11, Circle(), self.element_style)))
        self.play(tree.insert(TreeNode(21, Circle(), self.element_style)))
        self.play(tree.insert(TreeNode(22, Circle(), self.element_style)))
        self.play(tree.insert(TreeNode(23, Circle(), self.element_style)))
        self.play(tree.insert(TreeNode(24, Circle(), self.element_style)))
        self.play(tree.insert(TreeNode(25, Circle(), self.element_style)))
        self.play(tree.go_left(), tree.current_node.set_style(self.visited_style))
        self.play(tree.go_left(), tree.current_node.set_style(self.visited_style))

        target = 11
        

s = DFSScene()
s.construct()