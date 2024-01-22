from manim import *
from Array import Array
from LinkedList import LinkedList
from Pointer import Pointer
from Recursion import Recursion
from TreeElement import TreeElement
from Stack import Stack
from CodeWindow import CodeWindow
from VariableWindow import VariableWindow


class StackTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        arr = [5]
        code = """

        stack = Stack()
        stack.push(5)
        stack.push(9)
        stack.push(6)
        stack.pop()
        stack.push(4)
        stack.push(1)
        stack.pop()
        print(stack.peek())
        print(stack.is_empty())"""
        code_window = CodeWindow(self, code)
        variable_window = VariableWindow(
            {"stack": "", "i": "0", "j": "0"}, font_size=30
        )
        variable_window.to_corner(DOWN + LEFT)
        self.play(FadeIn(variable_window))
        code_window.code.to_corner(UP + LEFT)
        self.play(FadeIn(code_window.code))
        self.wait(1)

        stack = Stack(self, arr, side_length=0.8)
        stack.move_to((0, -3, 0))
        self.play(*stack.initial_animations(), code_window.highlight_line(1))

        self.play(stack.push(9), code_window.highlight_line(2))
        arr.append(9)
        self.play(stack.push(6), code_window.highlight_line(3))
        arr.append(6)
        self.play(stack.pop(), code_window.highlight_line(4))
        arr.pop()
        self.play(stack.push(4), code_window.highlight_line(5))
        arr.append(4)
        self.play(stack.push(1), code_window.highlight_line(6))
        arr.append(1)
        self.play(stack.pop(), code_window.highlight_line(7))
        arr.pop()


# manim -pql main.py TreeElementTestScene
class TreeElementTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        recursion = Recursion(self, [1, 2, 3])
        init_animations = recursion.divide_tree_element(
            recursion.current_subproblem, data={f"fibonacci_sum({3})": ""}, level=0
        )
        self.play(init_animations)
        self.fibonacci_sum(recursion, 3)
        self.wait(1)

    def fibonacci_sum(self, recursion, n, level=0):
        if n <= 0:
            self.play(recursion.current_subproblem.update_data({"0": ""}))
            if recursion.current_subproblem.parent:
                traverse_up_animation = recursion.traverse_up()
                self.play(traverse_up_animation)
            return 0
        elif n == 1:
            self.play(recursion.current_subproblem.update_data({"1": ""}))
            if recursion.current_subproblem.parent:
                traverse_up_animation = recursion.traverse_up()
                self.play(traverse_up_animation)
            return 1
        else:
            left_animations = recursion.divide_tree_element(
                recursion.current_subproblem,
                data={f"fibonacci_sum({n - 1})": ""},
                level=level,
            )
            self.play(left_animations)
            sum_1 = self.fibonacci_sum(recursion, n - 1, level + 1)
            right_animations = recursion.divide_tree_element(
                recursion.current_subproblem,
                data={f"fibonacci_sum({n - 2})": ""},
                level=level,
            )
            self.play(right_animations)
            sum_2 = self.fibonacci_sum(recursion, n - 2, level + 1)
            self.play(
                recursion.current_subproblem.update_data({f"{sum_1 + sum_2}": ""})
            )
            if recursion.current_subproblem.parent:
                traverse_up_animation = recursion.traverse_up()
                self.play(traverse_up_animation)
            return sum_1 + sum_2


class RecursionTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def construct(self):
        arr = [3, 1, 4, 8, 12, 9, 2]
        recursion = Recursion(self, arr)
        init_animation = recursion.initialize_array()
        self.play(init_animation)
        self.wait(1)

        # Start recursive traversal

        self.recursive_traverse(recursion, 0, len(arr))

    def recursive_traverse(self, recursion, i, j, level=0):
        if j - i <= 1:  # Base case, adjust as needed
            traverse_up_animation = recursion.traverse_up()
            self.play(traverse_up_animation)
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
        print(f"subp: {recursion.current_subproblem}")
        left_child = recursion.current_subproblem.children[0]
        right_child = recursion.current_subproblem.children[1]
        left_pointer = Pointer(
            scene=self,
            array_object=left_child,
            initial_position=0,
            name="l",
            scale=0.3,
            color="#336FD2",
            show_text=False,
        )
        right_pointer = Pointer(
            scene=self,
            array_object=right_child,
            initial_position=0,
            name="r",
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
                    array1=left_child, array2=right_child, index1=l, index2=r
                )
            )
            if left_child.elements[l].value < right_child.elements[r].value:
                self.play(
                    recursion.current_subproblem.change_value(
                        index=l + r, new_val=left_child.elements[l].value
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
                self.play(left_child.compare_size(l, 9999))
                self.play(
                    recursion.current_subproblem.change_value(
                        l + r, left_child.elements[l].value
                    )
                )
                l += 1
                self.play(left_pointer.update_position(l))
        elif r < len(right_child.elements):
            while r < len(right_child.elements):
                self.play(right_child.compare_size(r, 9999))
                self.play(
                    recursion.current_subproblem.change_value(
                        l + r, right_child.elements[r].value
                    )
                )
                r += 1
                self.play(right_pointer.update_position(r))
        self.play(left_pointer.delete(), right_pointer.delete())

        if recursion.current_subproblem.parent:
            traverse_up_animation = recursion.traverse_up()
            self.play(traverse_up_animation)
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
        array = Array(self, arr, side_length=0.8)
        initial_animations = array.initial_animations()
        array.to_edge(UP + LEFT)
        self.play(*initial_animations)
        self.play(array.append(3))
        arr.append(3)
        self.play(array.change_value(1, 10))
        arr[1] = 10

        i_pointer = Pointer(self, array, 0, "i", color="#990000", point_direction=LEFT)
        j_pointer = Pointer(self, array, 1, "j", color="#000099", point_direction=RIGHT)
        self.play(i_pointer.initialize())
        self.play(j_pointer.initialize())

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
                    swapped = True
                j += 1
                self.play(j_pointer.update_position(j))
            i += 1
            self.play(i_pointer.update_position(i))
            j = i + 1
            self.play(j_pointer.update_position(j))
