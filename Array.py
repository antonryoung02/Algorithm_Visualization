from manim import *
from Element import Element

class Array(VGroup):
    def __init__(self,*values, side_length=1.5, gap=0,**kwargs):
        super().__init__(**kwargs)
        self.array = [*values]
        self.elements = [Element(value, side_length) for value in values]
        self.gap = gap

    def initialize(self):
        for index, element in enumerate(self.elements):
            if index == 0:
                self.add(element)
            else:
                self.add(element.next_to(self.elements[index-1], RIGHT, buff=self.gap))
        animations = [FadeIn(element) for element in self.elements]
        return animations

    def append(self, value, side_length=1.5):
        new_element = Element(value, side_length)
        if self.elements:
            new_element.next_to(self.elements[-1], RIGHT, buff=self.gap)
        self.elements.append(new_element)
        self.add(new_element)
        return FadeIn(new_element)

    def prepend(self, value, side_length=1.5):
        new_element = Element(value)
        new_element.move_to(self.elements[0].get_center())

        shift_animations = self.shift_at_index(0, side_length)

        self.elements.insert(0, new_element)
        self.add(new_element)
        return AnimationGroup(*shift_animations, FadeIn(new_element))
    
    def shift_at_index(self, index, distance=1.5):
        shift_animations = []
        for i in range(index, len(self)):
            shift_animations.append(self[i].animate.shift(RIGHT * distance))
        return shift_animations

    def swap(self, index1, index2):
        if index1 >= len(self.elements) or index2 >= len(self.elements):
            print(f"Indexes out of range for length {len(self.elements)}: 1. {index1}, 2. {index2}")
            return
        elem1, elem2 = self.elements[index1], self.elements[index2]
        anim1 = elem1.animate.move_to(elem2.get_center())
        anim2 = elem2.animate.move_to(elem1.get_center())
        self.elements[index1], self.elements[index2] = elem2, elem1
        return AnimationGroup(anim1, anim2)

    def compare(self, index1, index2, equal_color="#00FF00", unequal_color="#0000FF"):
        pass
    
    def delete(self, index, side_length=1.5):
        element = self.elements[index]
        shift_animations = []
        for i in range(index+1, len(self.elements)):
            shift_animations.append(self.elements[i].animate.shift(LEFT * side_length))
        self.remove(element)

        self.elements = [elem for i, elem in enumerate(self.elements) if i != index]

        return AnimationGroup(*shift_animations, FadeOut(element))

    def get_length(self):
        return len(self.elements)



