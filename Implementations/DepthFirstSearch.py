from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Recursion.BinaryTree import BinaryTree
from Elements.TreeElement import TreeNode
from Recursion.PositionStrategies import BinaryTreePositioner
from Utils.TreeDS import binary_tree_from_list
from Indicator import Indicator
from Windows.CodeWindow import CodeWindow
from  Callbacks.ElementCallbacks import zoomToElementCallback, displayCodeElementCallback
code = """
def depth_of_tree(root):
    if root is None:
        return 0
    left_depth = depth_of_tree(root.left)
    right_depth = depth_of_tree(root.right)
    return max(left_depth, right_depth) + 1

""" 

# PYTHONPATH=$(pwd) manim -pql Implementations/DepthFirstSearch.py DFSScene
class DFSScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Circle:{"radius":0.5}, Text:{"font_size":30}}
        self.indicator_style={Circle:{"radius":0.5, "stroke_width":10, "color":BLUE}}
        self.visited_style={Circle:{"radius":0.5, "color":GREEN}, Text:{"font_size":30}}
        self.completed_style={Square:{"side_length":1, "color":GREEN}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}
        self.indicator = None 
        self.code_window = CodeWindow(code).set_opacity(0)

    def construct(self):
        values = ["_", "_", "_", "_", "_", "_", "_", "_","_", "_", None, "_", "_", None, None]
        elements = []
        for v in values:
            if v is None:
                elements.append(None)
            else:
                elements.append(TreeNode(v, Circle(), self.element_style))
        zte_callback = zoomToElementCallback(self.camera)
        dce_callback = displayCodeElementCallback(self.code_window, LEFT)
        elements[1].callbacks = [zte_callback, dce_callback]
        elements[4].callbacks = [zte_callback, dce_callback]

        positioner = BinaryTreePositioner(1.5, 4)
        tree = BinaryTree(elements, positioner)
        self.indicator = Indicator(tree, Circle(), self.indicator_style)

        self.play(self.code_window.create(), self.indicator.create(), tree.create(), tree.current_node.set_style(self.visited_style))
        root = binary_tree_from_list(values)
        self.find_max_depth(tree, root)
    
    def find_max_depth(self, tree, root):
        self.play(self.code_window.highlight(2))
        if root is None:
            self.play(self.code_window.highlight(3))
            return 0
        self.play(tree.current_node.set_style(self.visited_style))

        self.play(self.code_window.highlight(4)) 
        self.play(self.indicator.go_left())
        left_depth = self.find_max_depth(tree, root.left)
        
        self.play(self.code_window.highlight(5))
        self.play(self.indicator.go_right())
        right_depth = self.find_max_depth(tree, root.right)

        self.play(self.code_window.highlight(6))
        largest_depth = max(left_depth, right_depth) + 1 
        self.play(tree.current_node.set_data(str(largest_depth)), self.indicator.go_up())
        return largest_depth
        

s = DFSScene()
s.construct()