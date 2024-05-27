from Elements.Element import Element
from Elements.TreeElement import TreeElement
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion import Recursion
# PYTHONPATH=$(pwd) manim -pql Implementations/MergeSort.py MergesortScene
class MergesortScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator()

    def construct(self):
        data = [3, 1, 8, 4, 16, 5, 9, 7]
        elements = [Element(str(i), {"side_length":1}) for i in data]
        r = Recursion(elements)
        self.play(r.create())
        self.recursion(r, data, 0, len(data), 0)

    def recursion(self, array, data, i, j, level):
        if j - i <= 1:
            self.play(self.a.show_completed(array.current_subproblem))
            self.play(array.traverse_up())
            return [data[i]]
        
        midpt = (i + j) // 2 

        self.play(array.divide_array(array.current_subproblem, level, i, midpt))
        left_data = self.recursion(array, data, i, midpt, level + 1)

        self.play(array.divide_array(array.current_subproblem, level, midpt, j))
        right_data = self.recursion(array, data, midpt, j, level + 1)

        left_child = array.current_subproblem.children[0]
        right_child = array.current_subproblem.children[1]
        lp = Pointer(left_child, UP, style={"color":"red"}, name="i")
        rp = Pointer(right_child, UP, style={"color":"blue"}, name="j") 
        pp = Pointer(array.current_subproblem, UP, style={"color":"green"}, name="i+j")
        self.play(lp.create(), rp.create(), pp.create(), array.current_subproblem.clear_array())

        l = 0
        r = 0
        combined_data = []

        while l < len(left_data) and r < len(right_data):
            self.play(self.a.compare_size(l, r, left_child, right_child))
            if left_data[l] < right_data[r]:
                self.play(array.current_subproblem.elements[l+r].set_data(left_data[l]))
                combined_data.append(left_data[l])
                l += 1
                self.play(pp.update(l+r), lp.update(l))
            else:
                self.play(array.current_subproblem.elements[l + r].set_data(right_data[r]))
                combined_data.append(right_data[r])
                r += 1
                self.play(pp.update(l+r), rp.update(r))

        while l < len(left_data):
            self.play(self.a.indicate(l, left_child))
            self.play(array.current_subproblem.elements[l + r].set_data(left_data[l]))
            combined_data.append(left_data[l])
            l += 1
            self.play(pp.update(l+r), lp.update(l))

        while r < len(right_data):
            self.play(self.a.indicate(r, right_child))
            self.play(array.current_subproblem.elements[l+r].set_data(right_data[r]))
            combined_data.append(right_data[r])
            r += 1
            self.play(pp.update(l+r), rp.update(r))

        self.play(lp.delete(), rp.delete(), pp.delete())

        self.play(self.a.show_completed(array.current_subproblem))
        if array.current_subproblem.parent is not None:
            self.play(array.traverse_up())

        return combined_data
    
mss = MergesortScene()
mss.construct()