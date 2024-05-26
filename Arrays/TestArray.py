from Elements.Element import Element
from Elements.TreeElement import TreeElement
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
# PYTHONPATH=$(pwd) manim -pql Arrays/TestArray.py ArrayTestScene
class ArrayTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        elements = [Element(str(i), {"side_length":1}) for i in range(3)]
        # array = Array(elements)
        # self.add(array)
        # self.play(array.create())
        # self.wait(1)
        # self.play(array.change_element(1, data="20"))
        # self.wait(1)
        # self.play(array.remove_element(0))
        # # self.play(e.set_data({"val1": "6", "val2":"2"}))
        # self.wait(1)
        # self.play(array.change_element(2, data="12"))
        # self.wait(1)
        # self.play(array.insert_element(1, Element("23", {"side_length":1})))
        # self.wait(1)
        # self.play(array.remove_element(1))
        # self.wait(1)
        # self.play(array.delete())
        # self.wait(1)
        a = Animator()
        linked_list = LinkedList(elements)
        self.add(linked_list)
        self.play(linked_list.create())
        self.wait(1)
        self.play(linked_list.insert_element(2, Element("3", {"side_length":1})))

        self.play(linked_list.insert_element(1, Element("13", {"side_length":1})))
        self.play(linked_list.insert_element(0, Element("23", {"side_length":1})))
        linked_list.to_corner(UP + LEFT)
        #self.play(linked_list.remove_element(0))
        self.play(linked_list.remove_element(1))
        self.play(linked_list.remove_element(0))
        self.wait(1)
        llp = Pointer(linked_list, direction=UP, style={"color":"red"}, name="i")
        self.play(llp.create())
        self.play(llp.update(1))
        self.play(llp.update(2))
        self.play(llp.update(3))
        self.play(a.compare_if_equal(2, 0, linked_list))
        self.play(a.compare_size(1,2,linked_list))
        self.play(a.check_is_equal(1, 5, linked_list))
        self.wait(1)

ats = ArrayTestScene()
ats.construct()