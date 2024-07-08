from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from ArrayPointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Recursion.PositionStrategies import OneChildPositioner

code = """

"""
# TODO FIX LOOKS BAD


# PYTHONPATH=$(pwd) manim -pql Implementations/BinarySearch_704.py BinarySearchScene
class BinarySearchScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":1}, Text:{"font_size":30}}
        
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}
        self.marked_styles={Square:{"side_length":1, "color":BLUE}, Text:{"font_size":30}}

    def construct(self):
        nums = [-5, -2, -1, 0, 2, 4, 6, 7, 9]
        elements = [Element(n, Square(), self.element_style) for n in nums]
        array = Recursion(elements, OneChildPositioner(1.5))
        target = 0
        self.play(array.create())
        i = 0
        j = len(nums) - 1
        return self.binary_search(array, nums, target, i, j, 0)

    def binary_search(self, array, nums, target, i, j, level):
        if j - i == 0:
            self.play(self.a.check_is_equal(0, target, ))
            return -1 if nums[i] != target else i
        
        midpoint = (j + i) // 2
        array_mdpt = array.current_subproblem.get_midpt()

        self.play(self.a.check_size(array.current_subproblem.elements[array_mdpt], target))
        if nums[midpoint] > target:
            self.play(
                self.a.set_group_element_styles(range(array_mdpt), array.current_subproblem, self.marked_styles), 
                array.divide_array(array.current_subproblem, level, i, midpoint-1)
            )
            return self.binary_search(array, nums, target, i, midpoint-1, level+1)
        elif nums[midpoint] < target:
            self.play(
                self.a.set_group_element_styles(range(array_mdpt+1,len(array.current_subproblem)), array.current_subproblem, self.marked_styles), 
                array.divide_array(array.current_subproblem, level, midpoint + 1, j)
            )
            return self.binary_search(array, nums, target, midpoint + 1, j, level+1)
        else:
            self.play(self.a.check_is_equal(array.current_subproblem.elements[array_mdpt], target))
            return midpoint

s = BinarySearchScene()
s.construct()