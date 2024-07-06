from manim import VGroup, AnimationGroup, FadeIn, FadeOut, ORIGIN, RIGHT, LEFT
import numpy as np
from abc import ABC, abstractmethod

"""
Interface for defining a new Element class

set_data: updates the element's Text object. returns an animation

set_style: updates the appearance of the element's Text, Shape objects. returns an animation

equals: defines how to compare equality of 2 elements, or a string that can be inverted to original data type with the
element's parser.invert_parse(str) method.
 
less_than: defines how to check if element is less than another element or a string that can be inverted to 
original data type with the element's parser.invert_parse(str) method

greater_than: defines how to check if element is greater than another element or a string that can be inverted to 
original data type with the element's parser.invert_parse(str) method 

get_data: returns the original data passed to the element by calling parser.invert_parse(element.data.text)

create: Initializes the object to the scene. Returns an animation

delete: Removes the object from the scene. Returns an animation
"""

class AbstractElement(ABC, VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shape = None
        self.data = None

    @abstractmethod
    def set_data(self, new_data) -> None:
        pass

    @abstractmethod
    def set_style(self, new_style) -> None:
        pass

    @abstractmethod 
    def equals(self, other) -> None:
        pass

    @abstractmethod
    def less_than(self, other) -> None:
        pass

    @abstractmethod
    def greater_than(self, other) -> None:
        pass

    @abstractmethod
    def get_data(self) -> None:
        pass
    
    @abstractmethod
    def create(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass