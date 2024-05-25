from manim import VGroup, AnimationGroup, FadeIn, FadeOut, ORIGIN, RIGHT, LEFT
import numpy as np
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

    # def move_to(self, point_or_mobject, aligned_edge=ORIGIN, coor_mask=np.array([1, 1, 1]), **kwargs):
    #     super().move_to(point_or_mobject, aligned_edge=aligned_edge, coor_mask=coor_mask, **kwargs)
    #     self.shape.move_to(self.get_center())
    #     self.data.move_to(self.get_center())

    # def next_to(self, mobject_or_point, direction=RIGHT, buff=0.1, aligned_edge=None, submobject_to_align=None, index_of_submobject_to_align=None, coor_mask=np.array([1, 1, 1]), **kwargs):
    #     target_point = mobject_or_point.get_edge_center(direction) + 2* direction * buff
    #     self.move_to(target_point, aligned_edge= -1 * direction, coor_mask=coor_mask, **kwargs)
    #     return self
    
    # def get_edge_center(self, direction):
    #     return self.shape.get_edge_center(direction)

    # def shift(self, direction):
    #     print("override shift called")
    #     super().shift(direction)
    #     self.shape.shift(direction)
    #     self.data.shift(direction)

    # def animate_shift(self, direction):
    #     animations = [self.animate.shift(direction)]
    #     animations.append(self.shape.animate.shift(direction))
    #     animations.append(self.data.animate.shift(direction))
    #     return AnimationGroup(*animations)

    @abstractmethod
    def get_data(self) -> None:
        pass

    @abstractmethod
    def set_style(self, new_style) -> None:
        pass

    def create(self):
        return AnimationGroup(FadeIn(self.shape), FadeIn(self.data))

    def delete(self):
        return AnimationGroup(FadeOut(self.shape), FadeOut(self.data))
