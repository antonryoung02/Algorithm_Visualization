from manim import VGroup, AnimationGroup, FadeIn, FadeOut
from abc import ABC, abstractmethod

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
    def change_element(self, index, data, style) -> None:
        pass

    @abstractmethod
    def create(self, elements) -> None:
        pass

    @abstractmethod
    def get_element_at_index(self, index) -> None:
        pass

    def delete(self) -> None:
        return AnimationGroup(*[element.delete() for element in self.elements])

