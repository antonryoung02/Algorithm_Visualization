from Arrays.RecursiveArray import RecursiveArray
from Elements.Element import Element
from manim import *
from Recursion.PositionStrategies import BinaryTreePositioner

class BinaryTree(VGroup):
    """
    Assumes elements are an array represented with a level-order traversal
    """
    def __init__(self, elements, positioner):
        self.elements = elements
        self.positioner = positioner
        self.root = self.elements[0]
        self.current_node = self.root
        self._arrange_elements()

    def _arrange_elements(self):
        self.root.move_to(self.positioner.get_subproblem_position(self.root, 0))
        queue = [(self.root, 0)]
        i = 1

        while i < len(self.elements):
            current, level = queue.pop(0)

            if i < len(self.elements) and self.elements[i] is not None:
                current.set_left_child(self.elements[i])
                if current.left_child is not None:
                    current.left_child.move_to(self.positioner.get_subproblem_position(current.left_child, level + 1))
                    current.left_child.set_parent_arrow(CurvedArrow(current.get_bottom(), current.left_child.get_top(), angle=0))
                queue.append((current.left_child, level + 1))
            i += 1

            if i < len(self.elements) and self.elements[i] is not None:
                current.set_right_child(self.elements[i])
                if current.right_child is not None:
                    current.right_child.move_to(self.positioner.get_subproblem_position(current.right_child, level + 1))
                    current.right_child.set_parent_arrow(CurvedArrow(current.get_bottom(), current.right_child.get_top(), angle=0))
                queue.append((current.right_child, level + 1))
            i += 1

    def create(self):
        return AnimationGroup(*[element.create() for element in self.elements if element is not None])

    def _calculate_parent_with_index(self, index):
        if index == 0:
            return None 
        return self.elements[(index - 1) // 2]
    
    def _calculate_level_with_index(self, index):
        level = 0
        while (1 << level) <= index:
            level += 1
        return level - 1

    def level_order_insert(self, new_element):
        for i, element in enumerate(self.elements):
            if element is None:
                break
        else:
            i = len(self.elements)
            self.elements.append(None)

        self.elements[i] = new_element
        new_element.parent = self._calculate_parent_with_index(i)
        if not new_element.parent:
            return

        if new_element.parent.left_child is None:
            new_element.parent.set_left_child(new_element)
        else:
            new_element.parent.set_right_child(new_element)

        level = self._calculate_level_with_index(i)
        new_element.move_to(self.positioner.get_subproblem_position(new_element, level))
        if new_element.parent is not None:
            new_element.set_parent_arrow(CurvedArrow(new_element.parent.get_bottom(), new_element.get_top(), angle=0))
        return new_element.create()
