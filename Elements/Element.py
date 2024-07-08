from manim import *
from Elements.AbstractElement import AbstractElement
from Elements.ParsingFactories import ParserFactory

class Element(AbstractElement):
    def __init__(self, data, shape=Square, style={Square:{}, Text:{}}, callbacks=[], **kwargs):
        super().__init__(**kwargs)
        self._ensure_valid_init(shape, style, callbacks)
        self.style = style
        self.callbacks = callbacks
        self.shape = type(shape)(**self.style[type(shape)])
        self.parser = ParserFactory().create_parser(data)
        self.data = Text(self.parser.parse(data), **self.style[Text])
        self.add(self.shape, self.data)

    def set_data(self, new_data):
        before_set_data_animations = self.call_callback_hooks("before_set_data")
        old_data = self.data
        new_data = Text(self.parser.parse(new_data), **self.style[Text]).move_to(old_data)

        self.remove(old_data)
        self.add(new_data)
        self.data = new_data
        after_set_data_animations = self.call_callback_hooks("after_set_data")

        return Succession(before_set_data_animations, ReplacementTransform(old_data, new_data), after_set_data_animations, lag_ratio=1)
    
    def set_style(self, new_style):

        if type(self.shape) in new_style.keys():
            for key, val in new_style[type(self.shape)].items():
                self.style[type(self.shape)][key] = val
            new_shape = type(self.shape)(**self.style[type(self.shape)]).move_to(self.shape)
            old_shape = self.shape
            self.remove(old_shape)
            self.add(new_shape)
            self.shape = new_shape
            shape_transform = ReplacementTransform(old_shape, new_shape)
        else:
            shape_transform = Wait(0)

        if Text in new_style.keys():
            for key, val in new_style[Text].items():
                self.style[Text][key] = val
            new_data = Text(self.data.text, **self.style[Text]).move_to(self.data)
            old_data = self.data
            self.remove(old_data)
            self.add(new_data)
            self.data = new_data
            data_transform = ReplacementTransform(old_data, new_data)
        else:
            data_transform = Wait(0)

        return AnimationGroup(shape_transform, data_transform)

    def get_data(self):
        return self.parser.invert_parse(self.data.text)

    def equals(self, other):
        if other is None:
            return False
        if isinstance(other, Element):
            return self.parser.invert_parse(self.data.text) == other.parser.invert_parse(other.data.text)
        return self.parser.invert_parse(self.data.text) == self.parser.invert_parse(str(other))
    
    def less_than(self, other):
        if isinstance(other, Element):
            return self.parser.invert_parse(self.data.text) < other.parser.invert_parse(other.data.text)
        return self.parser.invert_parse(self.data.text) < self.parser.invert_parse(str(other))
    
    def greater_than(self, other):
        if isinstance(other, Element):
            return self.parser.invert_parse(self.data.text) > other.parser.invert_parse(other.data.text)
        return self.parser.invert_parse(self.data.text) > self.parser.invert_parse(str(other))
    
    def call_callback_hooks(self, method_name):
        animations = []
        for callback in self.callbacks:
            method = getattr(callback, method_name, None)
            if callable(method):
                animations.append(method(self))
            else:
                print(f"Warning: '{method_name}' method not found in {callback}")
        return AnimationGroup(*animations)
    
    def create(self):
        return AnimationGroup(FadeIn(self.shape), FadeIn(self.data), self.call_callback_hooks("on_create"))

    def delete(self):
        return AnimationGroup(FadeOut(self.shape), FadeOut(self.data), self.call_callback_hooks("on_delete"))
    
    def _ensure_valid_init(self, shape, style, callbacks):
        if not isinstance(shape, Mobject):
            raise TypeError(f"Argument shape expected to be Mobject. Got: {type(shape).__name__}")
        if type(shape) not in style.keys():
            raise ValueError(f"Expected {shape} key in style. Got keys: {list(style.keys())}")
        if Text not in style.keys():
            raise ValueError(f"Expected Manim.Text key in style. Got keys: {list(style.keys())}")
        for key in style.keys():
            if not isinstance(style[key], dict):
                raise TypeError(f"Expected value of 'style[{key}]' to be a dictionary. Got: {type(style[key]).__name__}")

