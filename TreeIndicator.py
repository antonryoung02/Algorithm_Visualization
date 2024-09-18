from manim import *

class Indicator(VGroup):
    def __init__(self, tree, shape, style, **kwargs):
        super().__init__(**kwargs)
        self.tree = tree
        self.style = style
        self.shape = type(shape)(**self.style[type(shape)])
        self.add(self.shape)

    def set_current_node(self, new_node):
        if not new_node:
            return Wait(0.1)
        target = new_node.val
        curr = None
        for element in self.tree.elements:
            if element.parser.invert_parse(element.data.text) == target:
                curr = element
                break
        self.tree.current_node = curr
        return self.shape.animate.move_to(curr)

    def create(self):
        self.move_to(self.tree.current_node)
        return FadeIn(self.shape)
    
    def delete(self):
        return FadeOut(self.shape)
   
    def go_left(self):
        current_node = self.tree.current_node
        if current_node.left_child is not None:
            end_visit_animations = current_node.call_callback_hooks("on_visit_end")
            self.tree.current_node = current_node.left_child
            start_visit_animations = current_node.left_child.call_callback_hooks("on_visit_start")
            return Succession(end_visit_animations, self.animate.move_to(self.tree.current_node), start_visit_animations)
        return Wait(0)

    def go_right(self):
        current_node = self.tree.current_node
        if current_node.right_child is not None:
            end_visit_animations = current_node.call_callback_hooks("on_visit_end")
            self.tree.current_node = current_node.right_child
            start_visit_animations = current_node.right_child.call_callback_hooks("on_visit_start")
            return Succession(end_visit_animations, self.animate.move_to(self.tree.current_node), start_visit_animations)
        return Wait(0)

    def go_up(self):
        current_node = self.tree.current_node
        if current_node.parent is not None:
            end_visit_animations = current_node.call_callback_hooks("on_visit_end")
            self.tree.current_node = current_node.parent
            start_visit_animations = current_node.parent.call_callback_hooks("on_visit_start")
            return Succession(end_visit_animations, self.animate.move_to(self.tree.current_node), start_visit_animations)
        return Wait(0)
    
    def set_style(self, style):
        self.style = style
        new_shape = type(self.shape)(**self.style[type(self.shape)]).move_to(self.shape)
        shape_transform = ReplacementTransform(self.pointer, new_shape)
        self.remove(self.shape)
        self.add(new_shape)
        self.shape = new_shape
        return shape_transform
    
