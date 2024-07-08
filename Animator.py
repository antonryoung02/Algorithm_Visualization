from manim import * 
import random

class Animator:
    def __init__(self, scene):
        self.scene = scene
    """Handles animations for all Element/Array types"""
    
    def compare_if_equal(self, element1, element2):
        if element1 is None or element2 is None:
            return Wait(0)
        shape_color = GREEN if element1.equals(element2) else RED
        animation1 = AnimatedBoundary(element1.shape, colors=[shape_color])
        animation2 = AnimatedBoundary(element2.shape, colors=[shape_color])
        return Succession(AnimationGroup(FadeIn(animation1), FadeIn(animation2)), Wait(0.4), AnimationGroup(FadeOut(animation1), FadeOut(animation2)))

    def check_is_equal(self, element, val):
        if element is None:
            return Wait(0)
        shape_color = GREEN if element.equals(val) else RED
        animation = AnimatedBoundary(element.shape, colors=[shape_color]) 
        return Succession(FadeIn(animation), Wait(0.4), FadeOut(animation))
    
    def check_size(self, element, val):
        if element is None:
            return Wait(0)
        if element.equals(val):
            return self.indicate(element)
        if element.greater_than(val):
            return Succession(
                AnimationGroup(element.shape.animate.scale(1.2)), 
                Wait(0),
                AnimationGroup(element.shape.animate.scale(1))
            )
        return Succession(
            AnimationGroup(element.shape.animate.scale(0.8)), 
            Wait(0),
            AnimationGroup(element.shape.animate.scale(1))
        ) 

    def indicate(self, element):
        if element is None:
            return Wait(0)
        return Indicate(element.shape, run_time=1)
    
    def compare_size(self, element1, element2):
        if element1 is None or element2 is None:
            return Wait(0)
        if element1.equals(element2):
            return Wait(0)
        if element1.greater_than(element2):
            return Succession(
                AnimationGroup(element1.shape.animate.scale(1.2), element2.shape.animate.scale(0.8)), 
                Wait(0),
                AnimationGroup(element1.shape.animate.scale(1), element2.shape.animate.scale(1))
            )
        return Succession(
            AnimationGroup(element2.shape.animate.scale(1.2), element1.shape.animate.scale(0.8)), 
            Wait(0),
            AnimationGroup(element2.shape.animate.scale(1), element1.shape.animate.scale(1))
        ) 

    def show_completed(self, array, color=GREEN):
        return AnimationGroup(*[element.animate.set_color(color) for element in array.elements])

    def set_group_element_styles(self, indices_list, array, new_style):
        return AnimationGroup(*[array.elements[index].set_style(new_style) for index in indices_list]) 

    def move_element_data_to_other(self, element, other, color=None):
        moving_data = element.data.copy()
        if color is not None:
            moving_data.set_color(color)
        moving_data.generate_target()
        moving_data.target.move_to(other)
        return Succession(MoveToTarget(moving_data), FadeOut(moving_data), lag_ratio=0.5)

    def sort(self, array):
        vals = [element.get_data() for element in array.elements]
        indexed_vals = list(enumerate(vals))
        sorted_vals = sorted(indexed_vals, key=lambda x: x[1])
        
        animations = []
        for new_index, (old_index, val) in enumerate(sorted_vals):
            element = array.elements[old_index]
            arc = (1 - random.random()) * 90 * DEGREES
            animations.append(Transform(element, element.copy().move_to(array.elements[new_index]), path_arc=arc))

        reordered_elements = [array.elements[old_index] for old_index, _ in sorted_vals]
        array.elements = reordered_elements
        return AnimationGroup(*animations, lag_ratio=0.1)

    def show_increase_element_data(self, element):
        return Succession(
            element.data.animate.scale(1.2), 
            Wait(0),
            element.data.animate.scale(1)
        )

    def show_decrease_element_data(self, element):
        return Succession(
            element.data.animate.scale(0.8), 
            Wait(0),
            element.data.animate.scale(1)
        )
        
    def show_math_then_set_data(self, element, math_str, new_data):
        self.scene.play(element.set_data(math_str))
        return element.set_data(new_data)
    
        
        

    # For graph, add outgoing edge animations
