from manim import *


class RecursiveElement(VGroup):
    def __init__(self, data, width=3.0, height=1.5, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.width = width
        self.height = height
        self.element = self.create_element()

    def create_element(self):
        rect = Rectangle(width=self.width, height=self.height)
        text_lines = [f"{key}: {value}" for key, value in self.data.items()]

        text = Text("\n".join(text_lines), font_size=24)
        text.move_to(rect.get_center())
        element = VGroup(rect, text)
        self.add(element)
        return element

    def update_data(self, new_data):
        self.data = new_data
        self.remove(self.element)
        self.element = self.create_element()
