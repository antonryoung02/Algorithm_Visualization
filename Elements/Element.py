from manim import *
from AbstractElement import AbstractElement


class Element(AbstractElement):
    def __init__(self, data:str, style:dict, **kwargs):
        super().__init__(**kwargs)
        self.shape = Square()
        self.data = Text(data)
        self.style = style
        self.add(self.shape, self.data)
        self.set_style(style)

    def _extract_shape_styles(self, new_style):
        keys = ["color", "height", "width"]
        return {key: new_style[key] for key in keys if key in new_style}

    def _extract_data_styles(self, new_style):
        keys = ["color", "font_size", "weight"]
        return {key: new_style[key] for key in keys if key in new_style}
    

    def set_style(self, new_style):
        self.style = new_style
        new_shape = Square(**self._extract_shape_styles(new_style))
        new_data = Text(self.data.text, **self._extract_data_styles(new_style)) 

        shape_transform = ReplacementTransform(self.shape, new_shape)
        data_transform = ReplacementTransform(self.data, new_data)

        self.shape = new_shape
        self.data = new_data
        return AnimationGroup(shape_transform, data_transform)

    def set_data(self, new_data):
        new_data_mobject = Text(new_data, **self._extract_data_styles(self.style))
        new_data_mobject.move_to(self.data)

        data_transform = ReplacementTransform(self.data, new_data_mobject)
        self.data = new_data_mobject
        return data_transform
    
    def get_data(self):
        return self.data.text
