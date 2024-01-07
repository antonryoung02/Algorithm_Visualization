from manim import *

class CodeWindow():
    """
    Displays and manages the code block displayed in the scene
    
    param scene: Scene drawing the animation
    file_path: Path to the displayed code file
    """
    def __init__(self, scene, file_path):
        self.scene = scene
        self.code = Code(
            file_path,
            style="monokai",
            language="python",
            tab_width=4,
            line_spacing=0.4,
            insert_line_no=False,
            font="American Typewriter"
        )
        self.code.scale(0.85).to_corner(UP + RIGHT, buff=0.3)
    
    def highlight_line(self, line_number, run_time=0.5):
        """Highlights specific line being executed during the visualization"""
        paragraph = self.code[2] #Location of code text objects 
        if 0 <= line_number < len(paragraph.submobjects):
            line_to_highlight = paragraph.submobjects[line_number]

            highlight_bg = BackgroundRectangle(line_to_highlight, fill_opacity=0.5, color="#778cd9")
            self.scene.play(FadeIn(highlight_bg), run_time=run_time)
            self.scene.wait(run_time)
            self.scene.play(FadeOut(highlight_bg), run_time=run_time)
        else:
            print(f"Line number {line_number} is out of range in the code paragraph.")

