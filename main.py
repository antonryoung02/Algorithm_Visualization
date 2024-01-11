from manim import *
from Array import Array
from LinkedList import LinkedList
from Pointer import Pointer
from Recursion import Recursion


# manim -pql main.py ArrayScene
class RecursionTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation_groups = []

    def construct(self):
        arr = [3, 1, 4, 8, 12, 9, 2]
        recursion = Recursion(self, arr)
        init_animation = recursion.initial_animations()
        self.play(init_animation)
        self.wait(1)

        # Start recursive traversal
        self.recursive_traverse(recursion, 0, len(arr))

    def recursive_traverse(self, recursion, i, j, level=0):
        if j - i <= 1:  # Base case, adjust as needed
            completed_animation = recursion.current_subproblem.show_completed()
            traverse_up_animation = recursion.traverse_up()
            self.play(completed_animation, traverse_up_animation)
            return
        midpt = (i + j) // 2
        left_animations = recursion.divide_array(
            recursion.current_subproblem, level, i, midpt
        )
        self.play(left_animations)
        self.recursive_traverse(recursion, i, midpt, level + 1)

        right_animations = recursion.divide_array(
            recursion.current_subproblem, level, midpt, j
        )
        self.play(right_animations)
        self.recursive_traverse(recursion, midpt, j, level + 1)

        # Inductive step solution animations.
        left_child = recursion.current_subproblem.children[0]
        right_child = recursion.current_subproblem.children[1]
        left_pointer = Pointer(
            self,
            left_child.elements,
            0,
            "l",
            scale=0.3,
            color="#336FD2",
            show_text=False,
        )
        right_pointer = Pointer(
            self,
            right_child.elements,
            0,
            "r",
            scale=0.3,
            color="#336FD2",
            show_text=False,
        )
        self.play(
            left_pointer.initialize(),
            right_pointer.initialize(),
            recursion.current_subproblem.clear_array(),
        )

        l = 0
        r = 0

        while l < len(left_child.elements) and r < len(right_child.elements):
            self.play(
                recursion.compare_size_in_different_arrays(
                    left_child, right_child, l, r
                )
            )
            if left_child.elements[l].value < right_child.elements[r].value:
                self.play(
                    recursion.current_subproblem.change_value(
                        l + r, left_child.elements[l].value
                    )
                )
                l += 1
                self.play(left_pointer.update_position(l))
            else:
                self.play(
                    recursion.current_subproblem.change_value(
                        l + r, right_child.elements[r].value
                    )
                )
                r += 1
                self.play(right_pointer.update_position(r))

        if l < len(left_child.elements):
            while l < len(left_child.elements):
                self.play(left_child.compare_size(l, -9999))
                self.play(
                    recursion.current_subproblem.change_value(
                        l + r, left_child.elements[l].value
                    )
                )
                l += 1
                self.play(left_pointer.update_position(l))
        elif r < len(right_child.elements):
            while r < len(right_child.elements):
                self.play(right_child.compare_size(r, -9999))
                self.play(
                    recursion.current_subproblem.change_value(
                        l + r, right_child.elements[r].value
                    )
                )
                r += 1
                self.play(right_pointer.update_position(r))
        self.play(left_pointer.delete(), right_pointer.delete())

        if recursion.current_subproblem.parent:
            completed_animation = recursion.current_subproblem.show_completed()
            traverse_up_animation = recursion.traverse_up()
            self.play(completed_animation, traverse_up_animation)
        else:
            self.play(recursion.current_subproblem.show_completed())
        return


class LinkedListTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        arr = [3, 7, 8, 1, 3, 8]
        linked_list = LinkedList(self, arr, side_length=2)
        init_animation = linked_list.initial_animations()
        linked_list.to_edge(LEFT)
        self.play(*init_animation)

        i_pointer = Pointer(linked_list.elements, self, 0, "i")

        linked_list.delete(1)

        linked_list.delete(1)

        linked_list.insert(1, 3)

        linked_list.delete(linked_list.get_length() - 1)

        linked_list.delete(0)

        linked_list.insert(2, 3)

        linked_list.insert(0, 1)

        linked_list.insert(1, 1)

        i_pointer.array = linked_list.elements
        i_pointer.update_position(1)

        i_pointer.update_position(2)
        i_pointer.update_position(3)

        i_pointer.update_position(4)

        i_pointer.update_position(5)


class ArrayTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        arr = [5, 1, 2, 0, 6]
        array = Array(self, arr)
        initial_animations = array.initial_animations()
        array.to_edge(UP + LEFT)
        self.play(*initial_animations)
        self.play(array.append(3))
        arr.append(3)
        self.play(array.change_value(1, 10))
        arr[1] = 10

        i_pointer = Pointer(self, array, 0, "i", color="#990000")
        j_pointer = Pointer(self, array, 1, "j", color="#000099")
        i_pointer.initialize()
        j_pointer.initialize()

        swapped = True
        

        i = 0
        while swapped:
            swapped = False
            j = i + 1
            while j < len(arr):
                self.play(array.compare_size_at_index(i, j))
                if arr[i] > arr[j]:
                    self.play(array.swap(i, j))
                    arr[i], arr[j] = arr[j], arr[i]
                    i_pointer.array_changed(array.elements)
                    j_pointer.array_changed(array.elements)
                    swapped = True
                j += 1
                j_pointer.update_position(j)
            i += 1
            i_pointer.update_position(i)
            j = i + 1
            j_pointer.update_position(j)
