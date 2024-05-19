from manim import VGroup, AnimationGroup, FadeIn, FadeOut
from abc import ABC, abstractmethod

class AbstractElement(ABC, VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shape = None
        self.data = None
        self.style = None

    @abstractmethod
    def set_data(self, new_data) -> None:
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_style(self, new_style) -> None:
        pass

    def create(self):
        return AnimationGroup(FadeIn(self.shape), FadeIn(self.data))

    def delete(self):
        return AnimationGroup(FadeOut(self.shape), FadeOut(self.data))
