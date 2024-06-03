from abc import ABC, abstractmethod

class AbstractPositioner(ABC):
    @abstractmethod
    def get_subproblem_position(self, elements, current_subproblem, spacing_dict) -> None:
        pass

class TwoChildrenPositioner(AbstractPositioner):
    def __init__(self, vertical_spacing=1.5, horizontal_spacing=1):
        self.vertical_spacing = vertical_spacing
        self.horizontal_spacing = horizontal_spacing


    def get_subproblem_position(self, elements, current_subproblem):
        parent = current_subproblem.parent
        if parent is None:
            return [0, 3, 0]

        total_sibling_width = 0.5 * elements[0].get_width() * len(parent.elements) * self.horizontal_spacing

        start_x = parent.get_center()[0] - (total_sibling_width) 
        x = start_x + (len(parent.children)) * 2 * total_sibling_width

        y = parent.get_center()[1] - self.vertical_spacing

        return [x, y, 0]
    
class OneChildPositioner(AbstractPositioner):
    def __init__(self, level_spacing, subproblem_spacing, subproblem_size):
        self.level_spacing = level_spacing
        self.subproblem_spacing = subproblem_spacing
        self.subproblem_size = subproblem_size

    def get_subproblem_position(self, elements, current_subproblem, level):
        parent = current_subproblem.parent
        branching_factor = 2
        if parent is None:
            return [0, 2, 0]

        x = parent.get_center()[0] 
        y = parent.get_center()[1] - 1.5

        return [x, y, 0]
    