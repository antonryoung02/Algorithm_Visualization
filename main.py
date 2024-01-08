from manim import *
from Array import Array
from LinkedList import LinkedList
from Pointer import Pointer
from Recursion import Recursion
#manim -pql main.py ArrayScene
class ArrayScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation_groups = []

    def construct(self):
        arr = [3, 7, 8, 1, 3, 8, 1, 9]
        recursion = Recursion(arr)
        init_animation = recursion.initialize()
        self.play(*init_animation)
        self.wait(1)

        # Start recursive traversal
        self.recursive_traverse(recursion, 0, len(arr))

        # Play all animation groups
        for anim_group in self.animation_groups:
            self.play(*anim_group)
            self.wait(1)

        #LINKED LIST METHODS
        #-----------------------------
        # linked_list = LinkedList(arr)
        # init_animation = linked_list.initialize()
        # linked_list.to_edge(LEFT)
        # self.play(*init_animation)

        # i_pointer = Pointer(linked_list.elements, self, 0, "i")
        # init_animation = i_pointer.initialize()
        # self.play(init_animation)
        # self.wait(1)
        # unlink, delete = linked_list.delete(1)
        # self.play(unlink)
        # self.wait(1)
        # self.play(delete)
        # unlink, delete = linked_list.delete(1)
        # self.play(unlink)
        # self.wait(1)
        # self.play(delete)
        # unlink, delete = linked_list.insert(1,3)
        # self.play(unlink)
        # self.wait(1)
        # self.play(delete)

        # unlink, delete = linked_list.delete(linked_list.get_length() - 1)
        # self.play(unlink)
        # self.wait(1)
        # self.play(delete)

        # unlink, delete = linked_list.delete(0)
        # self.play(unlink)
        # self.wait(1)
        # self.play(delete)

        # insert, shift = linked_list.insert(2,3)
        # self.play(shift)
        # self.wait(1)
        # insert, shift = linked_list.insert(0,1)
        # self.play(shift)
        # self.wait(1)
        # insert, shift = linked_list.insert(1,1)
        # self.play(insert)
        # self.wait(1)
        # self.play(shift)
        # self.wait(1)

        # i_pointer.array = linked_list.elements
        # self.play(i_pointer.update_position(1))
        # self.wait(1)
        # self.play(i_pointer.update_position(2))
        # self.play(i_pointer.update_position(3))
        # self.wait(1)
        # self.play(i_pointer.update_position(4))
        # self.wait(1)
        # self.play(i_pointer.update_position(5))
        # self.wait(1)

        #ARRAY METHODS
        #-----------------------------------
        # array = Array(*arr)
        # init_animation = array.initialize()
        # array.to_edge(UP+LEFT)
        # self.play(*init_animation)
        # self.wait(1)

        # i_pointer = Pointer(array, self, 0, "i")
        # init_animation = i_pointer.initialize()
        # self.play(init_animation)

        # self.play(array.delete(1))
        # self.play(array.append(5))
        # self.play(array.prepend(6))
        # self.play(array.delete(3))

        # self.wait(1)
        # self.play(i_pointer.update_position(1))
        # self.wait(1)
        # self.play(i_pointer.update_position(3))
        # self.wait(1)
        # self.play(i_pointer.update_position(0))


        # i_pointer.delete()
    
    def recursive_traverse(self, recursion, i, j, level=0):
        print(i)
        print(j)
        if j - i <= 1:  # Base case, adjust as needed
            #self.animation_groups.append(recursion.divide(recursion.current_subproblem, level, i, j))
            recursion.current_subproblem = recursion.current_subproblem.parent
            return
        midpt = (i + j) // 2
        print(f"Midpt {midpt}")
        left_animations = recursion.divide(recursion.current_subproblem, level, i, midpt)
        self.animation_groups.append(left_animations)
        self.recursive_traverse(recursion, i, midpt, level + 1)

        right_animations = recursion.divide(recursion.current_subproblem, level, midpt, j)
        self.animation_groups.append(right_animations)
        self.recursive_traverse(recursion, midpt, j, level + 1)

        if recursion.current_subproblem.parent:
            recursion.current_subproblem = recursion.current_subproblem.parent
        else:
            print("This is the root!")

        return
        

        
                    


