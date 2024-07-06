from manim import VGroup, AnimationGroup, FadeIn, FadeOut
from abc import ABC, abstractmethod

"""
Interface for defining a new Array class

insert_element: inserts a new element at index, returns an animation

remove_element: removes element at index, returns an animation



"""
class AbstractArray(ABC, VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.elements = None

    @abstractmethod
    def insert_element(self, index, new_element) -> None:
        pass

    @abstractmethod
    def remove_element(self, index) -> None:
        pass
    
    @abstractmethod
    def create(self, elements) -> None:
        pass

    def delete(self) -> None:
        return AnimationGroup(*[element.delete() for element in self.elements])

