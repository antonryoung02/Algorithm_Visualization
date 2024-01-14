from manim import *


# Rect isn't displaying
class RecursiveElement(VGroup):
    """
    Recursion oftentimes returns values instead of an array.
    This class lets you specify variables and their values.
    Implementation should let you divide and combine
    """

    def __init__(self, data: dict, width: float = 3.0, height: float = 1.5, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.width = width
        self.height = height
        self.element = self.create_element()

    def create_element(self) -> VGroup:
        rect = Rectangle(width=self.width, height=self.height)
        text_lines = [f"{key}: {value}" for key, value in self.data.items()]

        text = Text("\n".join(text_lines), font_size=24)
        text.move_to(rect.get_center())
        element = VGroup(rect, text)
        self.add(element)
        return element

    def update_data(self, new_data: dict):
        """Resets all data"""
        self.data = new_data
        self.remove(self.element)
        self.element = self.create_element()

    def initialize(self) -> FadeIn:
        return FadeIn(self)
