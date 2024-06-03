from Elements.Element import Element
from Arrays.Array import Array
from Arrays.LinkedList import LinkedList
from manim import * 
from Pointer import Pointer
from Animator import Animator
from Recursion.Recursion import Recursion


code = """
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        max_length_substring = 0
        while j < len(s):
            if s[j] in s[i:j]:
                i += 1
            else:
                max_length_substring = max(max_length_substring, j - i + 1)
                j += 1
        return max_length_substring
"""

# PYTHONPATH=$(pwd) manim -pql Implementations/SubstringWithoutDuplicates_3.py SubstringWithoutDuplicatesScene
class SubstringWithoutDuplicatesScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.a = Animator()
        self.element_style={Square:{"side_length":1}, Text:{"font_size":30}}
        self.window_element_style={Rectangle:{"width":3, "height":1}, Text:{"font_size":26}}

    def construct(self):
        s = "pwwkew"
        elements = [Element(c, Square(), self.element_style) for c in s]

        array = Array(elements)
        array.to_corner(UP+LEFT).shift(DOWN)
        title = Text("Longest Substring Without Repeating Characters", font_size=40).to_corner(UP+LEFT)
        ip = Pointer(array, UP, style={"color":"red"}, name="i")
        jp = Pointer(array, UP, style={"color":"blue"}, name="j")
        self.play(array.create(), ip.create(), jp.create(), FadeIn(title))

        i = 0; j = 0; max_length_substring = 0

        while j < len(s):
            if s[j] in s[i:j]:
                self.play(*[self.a.check_is_equal(c, -1, array) for c in range(i, j+1)])
                i += 1
                self.play(ip.update(i))
            else:
                self.play(*[self.a.compare_if_equal(c, c, array) for c in range(i, j+1)])
                max_length_substring = max(max_length_substring, j - i + 1)
                j += 1
                self.play(jp.update(j))
        return max_length_substring

s = SubstringWithoutDuplicatesScene()
s.construct()
        