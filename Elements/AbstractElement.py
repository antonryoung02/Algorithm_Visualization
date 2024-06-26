from manim import VGroup, AnimationGroup, FadeIn, FadeOut, ORIGIN, RIGHT, LEFT
import numpy as np
from abc import ABC, abstractmethod

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