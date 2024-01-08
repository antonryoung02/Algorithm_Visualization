from manim import *
from Array import Array

class Recursion(VGroup):
    def __init__(self, array, branching_factor=2, subproblem_size=2, **kwargs):
        super().__init__(**kwargs)
        self.array = array
        self.branching_factor = branching_factor
        self.recursive_tree = {}
        self.level_spacing = 1.5  # Vertical spacing between levels
        self.subproblem_spacing = 1.5 # Base horizontal spacing between subproblems
        self.top_offset = 1
        self.subproblem_size = subproblem_size
        self.root = None
        self.current_subproblem = None
    
    def initialize(self):
        init_animations = self.divide(None, 0, 0, len(self.array))
        return init_animations
    
    def divide(self, parent, level, i, j):
        if str(level) not in self.recursive_tree:
            self.recursive_tree[str(level)] = []

        subproblem = Array(*self.array[i:j], side_length=0.8, parent=parent)
        divide_animations = subproblem.initialize()

        if parent is not None:
            parent.children.append(subproblem)
            print(f"Parent: {parent.submobjects}")
        else:
            self.root = subproblem
            print("Parent: None")

        subproblem.parent = parent
        self.current_subproblem = subproblem
        self.add(subproblem)
        print(f"Subproblem: {subproblem.submobjects}")

        subproblem.move_to(self.calculate_position(i, j, level))
        if parent is not None: 
            divide_animations.append(FadeIn(CurvedArrow(parent.get_bottom(), subproblem.get_top(), angle=0)))

        self.recursive_tree[str(level)].append(subproblem)
        return divide_animations

    def calculate_position(self, i, j, level):
        parent = self.current_subproblem.parent
        print(parent)
        if parent is None:
            # Position the root at the center
            return np.array([0, 3, 0])
        num_children_elements = len(self.array) / ((self.subproblem_size) ** (level))
        self.subproblem_spacing = 6 / (level + 1)**1.1

        # Calculate horizontal position relative to the parent
        # Assuming equal spacing between siblings
        total_sibling_width = 0.8*num_children_elements 
        start_x = parent.get_center()[0] - total_sibling_width / 2
        x = start_x + (1.2 * self.subproblem_spacing * ((len(parent.children) - 1))/1.3)

        # Calculate vertical position
        y = parent.get_center()[1] - self.level_spacing

        return np.array([x, y, 0])
    # def calculate_position(self, level, index, i, j):
    #     num_subproblems = self.branching_factor ** level

    #     if level == 0:
    #         x = 0  # Center the root
    #     else:
    #         # Estimating width of each subproblem (assuming uniform width for simplicity)
    #         total_width = self.subproblem_spacing * (num_subproblems - 1) + (len(self.array)-1) * ((self.branching_factor/self.subproblem_size))**level
    #         start_x = -total_width / 2
    #         x = 0.5 + start_x + index * self.subproblem_spacing + 0.8*((i+j)// 2)

    #     y = 3 - 1.5 * (self.level_spacing * level)
    #     return np.array([x, y, 0])