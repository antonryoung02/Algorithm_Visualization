from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion
from Recursion.PositionStrategies import OneChildPositioner, TwoChildrenPositioner
from Callbacks.ElementCallbacks import zoomToElementCallback, displayCodeRecursionCallback, zoomToRecursionCallback
from Windows.CodeWindow import CodeWindow
# PYTHONPATH=$(pwd) manim -pql --disable_caching Implementations/MergeSort.py MergesortScene


code = """
    def merge_sort(self, array, i, j):
        # Base case 
        if j - i == 0: 
            return [array[i]]
        # Divide step
        midpt = (i + j) // 2
        left = merge_sort(array, i, midpt)
        right = merge_sort(array, midpt + 1, j)
        # Combine step
        lp = 0; rp = 0; new_arr = []
        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                new_arr.append(left[lp])
                lp += 1
            else:
                new_arr.append(right[rp])
                rp += 1
        while lp < len(left):
            new_arr.append(left[lp])
            lp += 1
        while rp < len(right):
            new_arr.append(right[rp])
            rp += 1
        return new_arr
"""
class MergesortScene(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator(self)
        self.element_style={Square:{"side_length":0.8}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}
        self.code_window = CodeWindow(code).set_opacity(0)

    def construct(self):
        data = ["3", "1", "8", "4", "6", "5", "9", "7"]
        data = ["9", "5", "6", "1"]
        elements = [Element(i, Square(), self.element_style, []) for i in data]
        recursion_positioner = TwoChildrenPositioner(1.3, 0.9)
        recursion_callback = displayCodeRecursionCallback(self.code_window, [1, 5, 6, 10], LEFT)
        recursion_zoom_callback = zoomToRecursionCallback(self, [1,5,6,10], 16)
        r = Recursion(elements, recursion_positioner, [recursion_zoom_callback, recursion_callback])
        self.play(r.create(), self.code_window.create())
        self.recursion(r, data, 0, len(data)-1, 0)

    def recursion(self, array, data, i, j, level):
        self.play(self.code_window.highlight(3))
        if j - i <= 0:
            self.play(self.code_window.highlight(4))
            self.play(self.a.show_completed(array.current_subproblem), array.traverse_up())
            return [data[i]]
        
        midpt = (i + j) // 2 
        self.play(self.code_window.highlight(6))
        self.play(self.code_window.highlight(7))
        self.play(array.divide_array(array.current_subproblem, level, i, midpt))
        left_data = self.recursion(array, data, i, midpt, level + 1)

        self.play(self.code_window.highlight(8))
        self.play(array.divide_array(array.current_subproblem, level, midpt+1, j))
        right_data = self.recursion(array, data, midpt+1, j, level + 1)

        left_child = array.current_subproblem.children[0]
        right_child = array.current_subproblem.children[1]

        lp = Pointer(left_child, UP, style={"color":"red"}, name="lp")
        rp = Pointer(right_child, UP, style={"color":"blue"}, name="rp") 
        pp = Pointer(array.current_subproblem, UP, style={"color":"green"}, name="lp+rp")
        self.play(self.code_window.highlight(10), lp.create(), rp.create(), pp.create(), array.current_subproblem.clear_array())

        l = 0
        r = 0
        combined_data = []

        while l < len(left_data) and r < len(right_data):
            self.play(self.code_window.highlight(12), self.a.compare_size(l, r, left_child, right_child))
            if left_data[l] < right_data[r]:
                self.play(self.code_window.highlight(13), array.current_subproblem.elements[l+r].set_data(left_data[l]))
                combined_data.append(left_data[l])
                l += 1
                self.play(self.code_window.highlight(14), pp.update(l+r), lp.update(l))
            else:
                self.play(self.code_window.highlight(16), array.current_subproblem.elements[l + r].set_data(right_data[r]))
                combined_data.append(right_data[r])
                r += 1
                self.play(self.code_window.highlight(17), pp.update(l+r), rp.update(r))

        while l < len(left_data):
            #self.play(self.a.indicate(l, left_child))
            self.play(self.code_window.highlight(19), array.current_subproblem.elements[l + r].set_data(left_data[l]))
            combined_data.append(left_data[l])
            l += 1
            self.play(self.code_window.highlight(20), pp.update(l+r), lp.update(l))

        while r < len(right_data):
            #self.play(self.a.indicate(r, right_child))
            self.play(self.code_window.highlight(22), array.current_subproblem.elements[l+r].set_data(right_data[r]))
            combined_data.append(right_data[r])
            r += 1
            self.play(self.code_window.highlight(23), pp.update(l+r), rp.update(r))

        self.play(lp.delete(), rp.delete(), pp.delete())


        self.play(self.code_window.highlight(24))
        if array.current_subproblem.parent is not None:
            self.play(self.a.show_completed(array.current_subproblem), array.traverse_up())
        else:
            self.play(self.a.show_completed(array.current_subproblem))

        return combined_data
    
mss = MergesortScene()
mss.construct()