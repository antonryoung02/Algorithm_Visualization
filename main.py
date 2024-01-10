from manim import *
from Array import Array
from LinkedList import LinkedList
from Pointer import Pointer
from Recursion import Recursion
#manim -pql main.py ArrayScene
class RecursionTestScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation_groups = []

    def construct(self):
        arr = [3, 7, 8, 1, 3, 8, 1, 9]
        recursion = Recursion(self, arr)
        init_animation = recursion.initial_animations()
        self.play(*init_animation)
        self.wait(1)

        # Start recursive traversal
        self.recursive_traverse(recursion, 0, len(arr))

        # Play all animation groups
        print(self.animation_groups)
        for anim_group in self.animation_groups:
            self.play(*anim_group)
            self.wait(1)
    
    def recursive_traverse(self, recursion, i, j, level=0):
        if j - i <= 1:  # Base case, adjust as needed
            #self.animation_groups.append(recursion.divide(recursion.current_subproblem, level, i, j))
            traverse_up_animation = recursion.traverse_up()
            self.animation_groups.append(traverse_up_animation)
            return
        midpt = (i + j) // 2
        left_animations = recursion.divide(recursion.current_subproblem, level, i, midpt)
        self.animation_groups.append(left_animations)
        self.recursive_traverse(recursion, i, midpt, level + 1)

        right_animations = recursion.divide(recursion.current_subproblem, level, midpt, j)
        self.animation_groups.append(right_animations)
        self.recursive_traverse(recursion, midpt, j, level + 1)

        if recursion.current_subproblem.parent:
            traverse_up_animation = recursion.traverse_up()
            self.animation_groups.append(traverse_up_animation)
        else:
            print("This is the root!")

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

        linked_list.insert(1,3)


        linked_list.delete(linked_list.get_length() - 1)

        linked_list.delete(0)

        linked_list.insert(2,3)

        linked_list.insert(0,1)

        linked_list.insert(1,1)


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
        array.to_edge(UP+LEFT)
        self.play(*initial_animations)
        array.append(3)
        arr.append(3)

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
                array.compare_size_at_index(i, j)
                if arr[i] > arr[j]:
                    array.swap(i, j)
                    arr[i], arr[j] = arr[j], arr[i]  # Swap the elements in the arr list
                    i_pointer.array_changed(array.elements)
                    j_pointer.array_changed(array.elements)
                    swapped = True
                j += 1
                j_pointer.update_position(j)
            i += 1
            i_pointer.update_position(i)
            j = i + 1
            j_pointer.update_position(j)



                        


