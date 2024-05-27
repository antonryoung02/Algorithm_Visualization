from manim import *
from Elements.AbstractElement import AbstractElement


class Element(AbstractElement):
    def __init__(self, data:str, style:dict, **kwargs):
        super().__init__(**kwargs)
        self.shape = Square()
        self.data = Text(str(data))
        self.style = style
        self.add(self.shape)
        self.add(self.data)
        self.set_style(style)

    def _extract_shape_styles(self, new_style):
        keys = ["color", "side_length"]
        return {key: new_style[key] for key in keys if key in new_style}

    def _extract_data_styles(self, new_style):
        keys = ["color", "font_size", "weight"]
        return {key: new_style[key] for key in keys if key in new_style}

    def _set_visible(self, new_obj):    
        """An easy way to delay showing the new object
        show with UpdateFromFunc(new_data_mobject, self.set_visible)
        """        
        new_obj.set_opacity(1)
    

    def set_style(self, new_style):
        self.style = new_style
        new_shape = Square(**self._extract_shape_styles(new_style))
        new_data = Text(self.data.text, **self._extract_data_styles(new_style)) 
        new_shape.move_to(self.shape)
        new_data.move_to(self.data)

        shape_transform = ReplacementTransform(self.shape, new_shape)
        data_transform = ReplacementTransform(self.data, new_data)

        self.remove(self.shape)
        self.remove(self.data)
        self.add(new_shape)
        self.add(new_data)
        self.shape = new_shape
        self.data = new_data
        return AnimationGroup(shape_transform, data_transform)

    def set_data(self, new_data):
        new_data_mobject = Text(str(new_data), **self._extract_data_styles(self.style))
        new_data_mobject.move_to(self.data)
        new_data_mobject.set_opacity(0)

        fade_out_old = FadeOut(self.data)

        self.remove(self.data)
        self.add(new_data_mobject)
        self.data = new_data_mobject

        return Succession(fade_out_old, UpdateFromFunc(new_data_mobject, self._set_visible))

    def get_data(self):
        return self.data.text

    def equals(self, other):
        if isinstance(other, Element):
            return self.data.text == other.data.text
        return self.data.text == str(other)
    
    def less_than(self, other):
        if isinstance(other, Element):
            return self.data.text < other.data.text
        return self.data.text < str(other)
    
    def greater_than(self, other):
        if isinstance(other, Element):
            return self.data.text > other.data.text
        return self.data.text > str(other)

