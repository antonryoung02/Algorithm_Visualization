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
from Utils.TreeDS import binary_tree_from_list

code = """

"""

# PYTHONPATH=$(pwd) manim -pql Implementations/DepthFirstSearch.py DFSScene
class DFSScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Circle:{"radius":0.5}, Text:{"font_size":30}}
        self.visited_style={Circle:{"radius":0.5, "color":GREEN}, Text:{"font_size":30}}
        self.completed_style={Square:{"side_length":1, "color":GREEN}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}

    def construct(self):
        values = ["_", "_", "_", "_", "_", "_", "_", "_","_", "_", None]
        elements = []
        for v in values:
            if v is None:
                elements.append(None)
            else:
                elements.append(TreeNode(v, Circle(), self.element_style))

        positioner = BinaryTreePositioner(1.5, 4)
        tree = BinaryTree(elements, positioner)
        self.play(tree.create(), tree.current_node.set_style(self.visited_style))
        root = binary_tree_from_list(values)
        self.find_max_depth(tree, root)
    
    def find_max_depth(self, tree, root):
        if root is None:
            return 0
        self.play(tree.current_node.set_style(self.visited_style))
        
        self.play(tree.go_left())
        left_depth = self.find_max_depth(tree, root.left)
        
        self.play(tree.go_right())
        right_depth = self.find_max_depth(tree, root.right)

        largest_depth = max(left_depth, right_depth) + 1 
        self.play(tree.current_node.set_data(str(largest_depth)), tree.go_up())
        return largest_depth
        

s = DFSScene()
s.construct()