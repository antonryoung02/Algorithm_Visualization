from manim import *
from Pointer import Pointer

class SlidingWindow:
    """
    Implements common functions of sliding window problems
    
    param array: Problem array input
    param scene: Scene drawing the animation
    """
    def __init__(self, array, scene:Scene):
        self.array = array
        self.scene = scene
        self.custom_texts = {}
        self.side_length = 12 / len(self.array) #Roughly fits all list items on screen for any length of array
        self.array_visual = self.initialize_array_visual()
        self.window_box = None
        self.i_pointer = Pointer(scene, self.array_visual, 0, "up", "#F87060", "i")
        self.j_pointer = Pointer(scene, self.array_visual, 0, "down", "#559CAD", "j")

    def initialize_array_visual(self):
        """Initializes the problem array visual object"""
        elements = [Square(side_length=self.side_length).add(Text(str(elem), font="Teko", font_size=24, color="#EDE6E3")) for elem in self.array]
        array_visual = VGroup(*elements).arrange(RIGHT, buff=0.25)
        array_visual.to_edge(DOWN, buff=1).to_edge(RIGHT, buff=0.5)
        return array_visual
    
    def initialize_pointers(self):
        """Draws the pointers to the screen at their initial positions"""
        self.i_pointer.initialize_pointer_visual()
        self.j_pointer.initialize_pointer_visual()

    def update_j_pointer(self, new_position:int):
        self.j_pointer.update_position(new_position)

    def update_i_pointer(self, new_position:int):
        self.i_pointer.update_position(new_position)

    def display_i_j_comparison(self, i_position, j_position):
        """
        Compares values at indices i and j.
        - Scales up the text of the compared elements, then scales them down, all in one go.
        """
        # Get text elements for i and j positions
        text_element_i = self.array_visual[i_position][1]
        text_element_j = self.array_visual[j_position][1]

        # Play all animations simultaneously
        self.scene.play(ScaleInPlace(text_element_j, 3), ScaleInPlace(text_element_i, 3))
        self.scene.wait(0.3)
        self.scene.play(ScaleInPlace(text_element_j, 1/3), ScaleInPlace(text_element_i, 1/3))



    def display_window_box(self, i_position, j_position):
        """
        Draws a transparent blue box over the array_visual between positions i and j.
        """
        if i_position > j_position or i_position < 0 or j_position >= len(self.array):
            raise ValueError("Invalid positions for window box.")

        i_element = self.array_visual[i_position]
        j_element = self.array_visual[j_position]

        if not self.window_box:
            self.window_box = Rectangle(
                width=j_element.get_right()[0] - i_element.get_left()[0],
                height=i_element.height,
                stroke_width=0,
                fill_color=BLUE,
                fill_opacity=0.5
            )
            self.window_box.stretch_to_fit_width(j_element.get_right()[0] - i_element.get_left()[0])
            self.window_box.move_to(i_element.get_left(), aligned_edge=LEFT)
            self.scene.play(Create(self.window_box, edge=LEFT))
        else:
            self.window_box.stretch_to_fit_width(j_element.get_right()[0] - i_element.get_left()[0])
            self.window_box.move_to(i_element.get_left(), aligned_edge=LEFT)

    def display_custom_variable(self, variable_name:str, variable_value, variable_color:str="#EDE6E3"):
        """
        Display or update a custom variable and its value on the screen.
        """
        # Create or update the variable name text
        name_text = Text(f"{variable_name}: ", font="Teko", color=variable_color).scale(0.7)

        # Create or update the variable value text
        value_text = Text(str(variable_value), font="Teko", color=variable_color).scale(0.7)
        
        if variable_name in self.custom_texts:
            # Update the existing value text
            existing_name_text, existing_value_text = self.custom_texts[variable_name]
            value_text.next_to(existing_name_text, RIGHT)  # Update position each time
            self.scene.play(Transform(existing_value_text, value_text))
        else:
            if self.custom_texts:
                # Position below the last text
                last_texts = list(self.custom_texts.values())[-1]
                name_text.next_to(last_texts[0], DOWN, aligned_edge=LEFT, buff=0.25)
            else:
                # First custom text positioned at the top left
                name_text.to_corner(UP + LEFT, buff=0.4)
            value_text.next_to(name_text, RIGHT)

            # Add the new texts to the scene
            self.scene.add(name_text, value_text)
            self.scene.play(Write(name_text, run_time=0.8), Write(value_text, run_time=0.8))
            self.custom_texts[variable_name] = (name_text, value_text)

