from manim import *
from Element import Element

class Array(VGroup):
    """
    Array class, provides common array manipulation methods

    values: an array of strings, floats, or ints
    side_length: size of element boxes
    gap: distance between each element 

    """
    def __init__(self, scene, values, side_length:float=1.5, gap:float=0.0, **kwargs):
        super().__init__(**kwargs)
        self.scene = scene
        self.array:List[int] = values
        self.elements:[Element] = [Element(value, side_length) for value in values]
        self.gap:float = gap
        self.side_length = side_length

        self.initialize()

    def initialize(self):
        for index, element in enumerate(self.elements):
            if index == 0:
                self.add(element)
            else:
                self.add(element.next_to(self.elements[index-1], RIGHT, buff=self.gap))

    def initial_animations(self):
        return [FadeIn(element) for element in self.elements]

    def append(self, value, side_length=1.5, animation_length=0.5):
        new_element = Element(value, side_length)
        if self.elements:
            new_element.next_to(self.elements[-1], RIGHT, buff=self.gap)
        self.elements.append(new_element)
        self.add(new_element)
        self.scene.play(FadeIn(new_element))
        self.scene.wait(animation_length)

    def prepend(self, value, side_length=1.5, animation_length=0.5):
        new_element = Element(value)
        new_element.move_to(self.elements[0].get_center())

        shift_animations = self.shift_at_index(0, side_length)

        self.elements.insert(0, new_element)
        self.add(new_element)
        self.scene.play(*shift_animations, FadeIn(new_element))
        self.scene.wait(animation_length)
    
    def shift_at_index(self, index, distance=1.5):
        """Helper method used in appending element. """
        shift_animations = []
        for i in range(index, len(self)):
            shift_animations.append(self[i].animate.shift(RIGHT * distance))
        return shift_animations

    def swap(self, index1, index2, animation_length=0.2):
        if index1 >= len(self.elements) or index2 >= len(self.elements):
            print(f"Indexes out of range for length {len(self.elements)}: 1. {index1}, 2. {index2}")
            return
        elem1, elem2 = self.elements[index1], self.elements[index2]
        anim1 = elem1.animate.move_to(elem2.get_center())
        anim2 = elem2.animate.move_to(elem1.get_center())
        self.elements[index1], self.elements[index2] = elem2, elem1
        self.scene.play(anim1, anim2)
        self.scene.wait(animation_length)
    
    def compare_equal_at_index(self, index1, index2, equal_colors="#00FF00", unequal_colors="#FF0000"):
        element1 = self.elements[index1]
        element2 = self.elements[index2]
        boundary_color = equal_colors if element1.value == element2.value else unequal_colors

        boundary1 = AnimatedBoundary(element1.square, colors=[boundary_color], cycle_rate=3)
        boundary2 = AnimatedBoundary(element2.square, colors=[boundary_color], cycle_rate=3)
        
        self.scene.add(boundary1, boundary2)
        self.scene.wait(1)
        self.scene.remove(boundary1, boundary2)

    def compare_value_equal(self, index, val, equal_colors="#00FF00", unequal_colors="#FF0000"):
        element = self.elements[index]
        boundary_color = equal_colors if element.value == val else unequal_colors

        boundary = AnimatedBoundary(element.square, colors=boundary_color, cycle_rate=3)
        
        self.scene.add(boundary)
        self.scene.wait(1)
        self.scene.remove(boundary)

    def compare_size_value(self, index, val):
        element = self.elements[index]

        if element.value < val:
            text_animation = ScaleInPlace(element.text, 0.5)
            scale_back_animation = ScaleInPlace(element.text, 2)
        else:
            text_animation = ScaleInPlace(element.text, 1.5)
            scale_back_animation = ScaleInPlace(element.text, 2/3)

        self.scene.play(text_animation)
        self.scene.wait(0.2)
        self.scene.play(scale_back_animation)

    
    def compare_size_at_index(self, index1, index2):
        element1 = self.elements[index1]
        element2 = self.elements[index2]

        if element1.value < element2.value:
            smaller_text_animation = ScaleInPlace(element1.text, 0.5)
            larger_text_animation = ScaleInPlace(element2.text, 1.5)
            scale_back_smaller = ScaleInPlace(element1.text, 2)  # Scale up to original size
            scale_back_larger = ScaleInPlace(element2.text, 2/3)  # Scale down to original size
        else:
            smaller_text_animation = ScaleInPlace(element2.text, 0.5)
            larger_text_animation = ScaleInPlace(element1.text, 1.5)
            scale_back_smaller = ScaleInPlace(element2.text, 2)
            scale_back_larger = ScaleInPlace(element1.text, 2/3)

        # Play the scaling animations simultaneously, and then scale back after a delay
        scaling_animations = AnimationGroup(smaller_text_animation, larger_text_animation)
        scale_back_animations = AnimationGroup(scale_back_smaller, scale_back_larger)
        
        self.scene.play(scaling_animations)
        self.scene.play(scale_back_animations)
        
        
    def delete(self, index, side_length=1.5, animation_length=0.5):
        element = self.elements[index]
        shift_animations = []
        for i in range(index+1, len(self.elements)):
            shift_animations.append(self.elements[i].animate.shift(LEFT * side_length))
        self.remove(element)

        self.elements = [elem for i, elem in enumerate(self.elements) if i != index]

        self.scene.play(*shift_animations, FadeOut(element))
        self.scene.wait(animation_length)

    def get_length(self):
        return len(self.elements)



