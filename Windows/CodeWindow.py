from manim import *


class CodeWindow(VGroup):
    """
    Displays and manages the code block displayed in the scene
    """

    def __init__(self, code, **kwargs):
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
        self.add(self.code)

    def create(self):
        return FadeIn(self.code)

    def highlight(self, line_number):
        """Highlights specific line being executed during the visualization if visible"""
        if self.fill_opacity == 0:
            return Wait(0.1)
        
        code_paragraph = self.code.submobjects[2]  # Accessing the Paragraph object
        if 0 <= line_number - 1 < len(code_paragraph.submobjects):
            line_to_highlight = code_paragraph.submobjects[line_number - 1]

            highlight_bg = BackgroundRectangle(
                line_to_highlight, fill_opacity=0.5, color="#778cd9"
            )
            return Succession(
                Create(highlight_bg), Wait(0.8), Uncreate(highlight_bg)
            )
        else:
            print(f"Line number {line_number - 1} is out of range in the code paragraph.")
            return Wait(0.1)
