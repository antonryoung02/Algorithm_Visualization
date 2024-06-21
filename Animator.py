from manim import * 

class Animator:
    def __init__(self, scene):
        self.scene = scene
    """Handles animations for all Element/Array types"""
    
    def compare_if_equal(self, index1, index2, array1, array2=None):
        element1 = array1.get_element_at_index(index1)
        if array2 is None:
            element2 = array1.get_element_at_index(index2)
        else:
            element2 = array2.get_element_at_index(index2)

        shape_color = GREEN if element1.equals(element2) else RED
        animation1 = AnimatedBoundary(element1.shape, colors=[shape_color])
        animation2 = AnimatedBoundary(element2.shape, colors=[shape_color])
        return Succession(AnimationGroup(FadeIn(animation1), FadeIn(animation2)), Wait(0.4), AnimationGroup(FadeOut(animation1), FadeOut(animation2)))

    def check_is_equal(self, index, val, array):
        element = array.get_element_at_index(index)
        shape_color = GREEN if element.equals(val) else RED
        animation = AnimatedBoundary(element.shape, colors=[shape_color]) 
        return Succession(FadeIn(animation), Wait(0.4), FadeOut(animation))
    
    def check_size(self, index, val, array):
        element = array.get_element_at_index(index)

        if element.equals(val):
            return self.indicate(index, array)

        if element.greater_than(val):
            return Succession(
                AnimationGroup(element.shape.animate.scale(1.2)), 
                Wait(0.1),
                AnimationGroup(element.shape.animate.scale(1))
            )
        return Succession(
            AnimationGroup(element.shape.animate.scale(0.8)), 
            Wait(0.1),
            AnimationGroup(element.shape.animate.scale(1))
        ) 

    def indicate(self, index, array):
        element = array.get_element_at_index(index)
        if element:
            return Indicate(element.shape, run_time=1)
        return Wait(0.1)
    
    def compare_size(self, index1, index2, array1, array2=None):
        element1 = array1.get_element_at_index(index1)
        element2 = array1.get_element_at_index(index2) if array2 is None else array2.get_element_at_index(index2)

        if element1.equals(element2):
            return AnimationGroup(
                self.indicate(index1, array1),
                self.indicate(index2, array2 if array2 else array1)
            )

        if element1.greater_than(element2):
            return Succession(
                AnimationGroup(element1.shape.animate.scale(1.2), element2.shape.animate.scale(0.8)), 
                Wait(0.1),
                AnimationGroup(element1.shape.animate.scale(1), element2.shape.animate.scale(1))
            )
        return Succession(
            AnimationGroup(element2.shape.animate.scale(1.2), element1.shape.animate.scale(0.8)), 
            Wait(0.1),
            AnimationGroup(element2.shape.animate.scale(1), element1.shape.animate.scale(1))
        ) 

    def show_completed(self, array):
        return AnimationGroup(*[element.animate.set_color(GREEN) for element in array.elements])

    def set_group_element_styles(self, indices_list, array, new_style):
        return AnimationGroup(*[array.get_element_at_index(index).set_style(new_style) for index in indices_list]) 

    def move_element_data_to_other(self, element, other):
        moving_data = element.data.copy()
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
            animations.append(element.animate.move_to(array.get_element_at_index(new_index)))

        reordered_elements = [array.elements[old_index] for old_index, _ in sorted_vals]
        array.elements = reordered_elements
        return AnimationGroup(*animations)


