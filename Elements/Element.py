from manim import *
from Elements.AbstractElement import AbstractElement
from Elements.ParsingFactories import ParserFactory

class Element(AbstractElement):
    def __init__(self, data, shape=Square, style={Square:{}, Text:{}}, **kwargs):
        super().__init__(**kwargs)
        self._ensure_valid_init(shape, style)
        self.style = style
        self.shape = type(shape)(**self.style[type(shape)])
        self.parser = ParserFactory().create_parser(data)
        self.data = Text(self.parser.parse(data), **self.style[Text])
        self.add(self.shape, self.data)

    def set_data(self, new_data):
        old_data = self.data
        new_data = Text(self.parser.parse(new_data), **self.style[Text]).move_to(old_data)

        self.remove(old_data)
        self.add(new_data)
        self.data = new_data

        return ReplacementTransform(old_data, new_data)
    
    def set_style(self, new_style):
        self.style = new_style
        old_shape = self.shape
        old_data = self.data
    
        new_shape = type(self.shape)(**self.style[type(self.shape)]).move_to(self.shape)
        new_data = Text(self.data.text, **self.style[Text]).move_to(self.data)

        self.remove(old_shape)
        self.remove(old_data)
        self.add(new_shape)
        self.add(new_data)
        self.shape = new_shape
        self.data = new_data
        return AnimationGroup(ReplacementTransform(old_shape, new_shape), ReplacementTransform(old_data, new_data))

    def get_data(self):
        return self.parser.invert_parse(self.data.text)

    def equals(self, other):
        if isinstance(other, Element):
            return self.parser.invert_parse(self.data.text) == other.parser.invert_parse(other.data.text)
        return self.data.text == str(other)
    
    def less_than(self, other):
        if isinstance(other, Element):
            return self.parser.invert_parse(self.data.text) < other.parser.invert_parse(other.data.text)
        return self.data.text < str(other)
    
    def greater_than(self, other):
        if isinstance(other, Element):
            return self.parser.invert_parse(self.data.text) > other.parser.invert_parse(other.data.text)
        return self.data.text > str(other)
    
    def _ensure_valid_init(self, shape, style):
        if not isinstance(shape, Mobject):
            raise TypeError(f"Argument shape expected to be Mobject. Got: {type(shape).__name__}")
        if type(shape) not in style.keys():
            raise ValueError(f"Expected {shape} key in style. Got keys: {list(style.keys())}")
        if Text not in style.keys():
            raise ValueError(f"Expected Manim.Text key in style. Got keys: {list(style.keys())}")
        for key in style.keys():
            if not isinstance(style[key], dict):
                raise TypeError(f"Expected value of 'style[{key}]' to be a dictionary. Got: {type(style[key]).__name__}")

