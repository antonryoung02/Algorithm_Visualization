from manim import *
from Elements.AbstractElement import AbstractElement

class WindowElement(AbstractElement):
    """Assumption is that each element contains a (key, val) tuple to track a variable"""
    def __init__(self, data:tuple, style:dict, **kwargs):
        super().__init__(**kwargs)
        self.shape = Rectangle(height=1, width=3)
        self.key = data[0]
        self.val = data[1]
        self.style = style
        self.data = Text(f"{self.key} = {self.val}", font_size=26)
        self.add(self.shape)
        self.add(self.data)
    
    def set_style(self, new_style):
        return

    def _set_visible(self, new_obj):          
        new_obj.set_opacity(1)

    def set_data(self, new_data):
        self.key = new_data[0]
        self.val = new_data[1]
        new_data_mobject = Text(f"{self.key} = {self.val}", font_size=26)
        new_data_mobject.move_to(self.data)
        new_data_mobject.set_opacity(0)

        fade_out_old = FadeOut(self.data)

        self.remove(self.data)
        self.add(new_data_mobject)
        self.data = new_data_mobject

        return Succession(fade_out_old, UpdateFromFunc(new_data_mobject, self._set_visible))
    
    def get_data(self):
        return {self.key:self.val}

    def equals(self, other_val):
        return self.val == other_val
    
    def less_than(self, other_val):
        return self.val < other_val
    
    def greater_than(self, other_val):
        return self.val > other_val

