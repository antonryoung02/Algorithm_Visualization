from manim import *


class CodeWindow(VGroup):
    """
    Displays and manages the code block displayed in the scene
    """

    def __init__(self, code, scale_bg_height=2.1, **kwargs):
        super().__init__(**kwargs)
        self.code = Code(
            code=code,
            style="github-dark",
            language="python",
            tab_width=4,
            font_size=12,
            line_spacing=1,
            insert_line_no=True,
            font="American Typewriter",
        )
        self.scale_bg_height = scale_bg_height
        self.add(self.code)

    def create(self):
        return FadeIn(self.code)

    def highlight(self, lines, animation_time=0.5):
        """Highlights specific line being executed during the visualization if visible"""
        if self.fill_opacity == 0:
            return Wait(0)
        
        if not isinstance(lines, list):
            lines = [lines]

        animations = []
        
        code_paragraph = self.code.submobjects[2]  # Accessing the Paragraph object
        line_height = code_paragraph.submobjects[0].height * self.scale_bg_height
        for line_number in lines:
            if 0 <= line_number - 1 < len(code_paragraph.submobjects):
                line_to_highlight = code_paragraph.submobjects[line_number - 1]

                highlight_bg = BackgroundRectangle(
                    line_to_highlight, fill_opacity=0.5, color="#778cd9"
                ).stretch_to_fit_height(line_height).shift(0.1*DOWN)
                animations.append(Succession(
                    Create(highlight_bg), Wait(animation_time), Uncreate(highlight_bg)
                ))
            else:
                print(f"Line number {line_number - 1} is out of range in the code paragraph.")
                animations.append(Wait(0.1))

        return AnimationGroup(*animations)
