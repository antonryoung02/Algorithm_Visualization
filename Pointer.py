from manim import *

class Pointer():
    """
    Manages an arrow object that traverses an algorithm's array.
    
    param scene: Scene drawing the animation
    array_visual: Problem array visual object
    position: Pointer index
    orientation: Pointer direction
    color: Pointer color
    name: Pointer's variable name defined in the problem code
    """
    def __init__(self, scene:Scene, array_visual:VGroup, position:int, orientation:str, color:str, name:str):
        self.position = position
        self.orientation = orientation
        self.color = color
        self.array_visual = array_visual
        self.scene = scene
        self.name = name
        self.pointer_visual = None
        self.pointer_info = None
    
    def initialize_pointer_visual(self):
        """Initializes the visual object and corresponding info"""
        if self.orientation == "up":
            start_point, end_point = DOWN, UP
        else:
            start_point, end_point = UP, DOWN
        self.pointer_visual = Arrow(start_point, end_point, color=self.color).scale(0.5)
        self.pointer_visual.next_to(self.array_visual[0], start_point)
        self.scene.play(Create(self.pointer_visual))
        self.pointer_info = self.display_info()

    def update_position(self, new_position:int):
        """Updates pointer position"""
        if self.position != new_position:
            self.scene.remove(self.pointer_info)

            self.animate_movement(new_position)
            self.position = new_position
            self.pointer_info = self.display_info()

    def animate_movement(self, new_position:int):
        """Animates the pointer moving to the new position"""
        new_location = self.pointer_visual.copy().next_to(self.array_visual[new_position], (UP if self.orientation == "down" else DOWN))
        self.scene.play(Transform(self.pointer_visual, new_location, run_time=0.2))

    def display_info(self):
        """Displays pointer label and value"""
        value = self.position
        text_str = f"{self.name} = {value}"
        text_object = Text(text_str, color=self.color, font="Teko").scale(0.5)

        text_object.next_to(self.pointer_visual, RIGHT)

        self.scene.add(text_object)
        self.scene.play(Write(text_object), run_time=0.1)

        return text_object



