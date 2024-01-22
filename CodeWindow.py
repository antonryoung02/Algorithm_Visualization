from manim import *


class CodeWindow(VGroup):
    """
    Displays and manages the code block displayed in the scene

    param scene: Scene drawing the animation
    file_path: Path to the displayed code file
    """

    def __init__(self, scene, code, file_path="stack_demo.py"):
        self.scene = scene
        self.code = Code(
            code=code,
            style="monokai",
            language="python",
            tab_width=4,
            line_spacing=0.4,
            insert_line_no=True,
            font="American Typewriter",
        )
        self.code.scale(0.85).to_corner(UP + RIGHT, buff=0.3)

    def highlight_line(self, line_number, run_time=0.1):
        """Highlights specific line being executed during the visualization"""
        code_paragraph = self.code.submobjects[2]  # Accessing the Paragraph object

        if 0 <= line_number < len(code_paragraph.submobjects):
            line_to_highlight = code_paragraph.submobjects[line_number]

            highlight_bg = BackgroundRectangle(
                line_to_highlight, fill_opacity=0.5, color="#778cd9"
            )
            return Succession(
                FadeIn(highlight_bg), Wait(run_time), FadeOut(highlight_bg)
            )
        else:
            print(f"Line number {line_number} is out of range in the code paragraph.")
            return Succession(Wait(0.1))
