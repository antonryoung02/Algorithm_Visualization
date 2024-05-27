from manim import *


class CodeWindow(VGroup):
    """
    Displays and manages the code block displayed in the scene
    """

    def __init__(self, code, **kwargs):
        super().__init__(**kwargs)
        self.code = Code(
            code=code,
            style="monokai",
            language="python",
            tab_width=4,
            font_size=14,
            line_spacing=1,
            insert_line_no=True,
            font="American Typewriter",
        )
        self.add(self.code)

    def create(self):
        return FadeIn(self.code)

    def highlight(self, line_number):
        """Highlights specific line being executed during the visualization"""
        code_paragraph = self.code.submobjects[2]  # Accessing the Paragraph object

        if 0 <= line_number - 1 < len(code_paragraph.submobjects):
            line_to_highlight = code_paragraph.submobjects[line_number - 1]

            highlight_bg = BackgroundRectangle(
                line_to_highlight, fill_opacity=0.5, color="#778cd9"
            )
            return Succession(
                FadeIn(highlight_bg, run_time=0.5), Wait(0.3), FadeOut(highlight_bg, run_time=0.5)
            )
        else:
            print(f"Line number {line_number - 1} is out of range in the code paragraph.")
            return Wait(0.1)
