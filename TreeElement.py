from manim import *


class TreeElement(VGroup):
    """
    Recursion oftentimes returns values instead of an array.
    This class lets you specify variables and their values.
    Implementation should let you divide and combine
    """

    # width is 0?
    def __init__(
        self,
        data: dict,
        parent=None,
        side_width=3,
        side_height=1,
        font_size=16,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.data = data
        self.side_width = side_width
        self.side_height = side_height
        self.font_size = font_size
        self.rect, self.text = self.create_element()
        self.add(self.rect, self.text)

        self.parent = parent
        self.children = []
        self.parent_arrow = None

    def create_element(self):
        rect = Rectangle(width=self.side_width, height=self.side_height)
        text_lines = [f"{key}: {value}" for key, value in self.data.items()]

        text = Text("\n".join(text_lines), font_size=self.font_size)
        text.move_to(rect.get_center())
        return rect, text

    def update_data(self, new_data: dict):
        """Updates the data and refreshes the text without changing the position."""
        self.data = new_data
        # Create a new text object with updated data
        new_text_lines = [f"{key}: {value}" for key, value in self.data.items()]
        new_text = Text("\n".join(new_text_lines), font_size=16)
        new_text.move_to(self.rect.get_center())

        # Update the existing text object
        old_text = self.text
        self.text = new_text

        # Add the new text to the group and remove the old text
        self.add(self.text)
        self.remove(old_text)

        # Return a transformation animation
        return Transform(old_text, self.text)

    # Copied from RecursiveArray.py
    def initialize(self) -> FadeIn:
        return FadeIn(self)

    def set_parent(self, new_parent):
        self.parent = new_parent

    def set_parent_arrow(self, parent_arrow):
        prev_arrow = self.parent_arrow
        self.parent_arrow = parent_arrow

        if prev_arrow is None:
            return FadeIn(self.parent_arrow)
        return Transform(prev_arrow, self.parent_arrow)

    def show_completed(self):
        color_animations = []
        for element in self.elements:
            color_animations.append(FadeToColor(element.square, "#00FF00"))

        return AnimationGroup(*color_animations)
