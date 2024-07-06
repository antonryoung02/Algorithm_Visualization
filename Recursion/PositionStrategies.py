class BinaryTreePositioner:
    def __init__(self, vertical_spacing=1, horizontal_spacing=4, depth_spacing=1.8):
        self.vertical_spacing = vertical_spacing
        self.horizontal_spacing = horizontal_spacing
        self.depth_spacing = depth_spacing

    def get_subproblem_position(self, current_subproblem, level): 
        #level is needed in the binaryTreePositioner to gradually narrow child widths
        if current_subproblem is None:
            return [0,0,0]
        parent = current_subproblem.parent
        if parent is None:
            return [0, 3, 0]

        total_sibling_width = 0.5 * current_subproblem.get_width() * (5/(level+1)**self.depth_spacing) * self.horizontal_spacing
        start_x = parent.get_center()[0] - total_sibling_width
        x = start_x + self._get_spacing_for_child(current_subproblem) * 2 * total_sibling_width
        y = parent.get_center()[1] - self.vertical_spacing
        return [x, y, 0]
    
    def _get_spacing_for_child(self, current_subproblem):
        if current_subproblem.parent.left_child is None:
            return 1
        if id(current_subproblem.parent.left_child) != id(current_subproblem):
            return 1
        return 0
    
class TwoChildrenPositioner:
    def __init__(self, vertical_spacing=1.5, horizontal_spacing=1):
        self.vertical_spacing = vertical_spacing
        self.horizontal_spacing = horizontal_spacing

    def get_subproblem_position(self, current_subproblem):
        parent = current_subproblem.parent
        if parent is None:
            return [0, 3, 0]

        total_sibling_width = 0.5 * current_subproblem.elements[0].get_width() * len(parent.elements) * self.horizontal_spacing
        start_x = parent.get_center()[0] - total_sibling_width
        x = start_x + len(parent.children) * 2 * total_sibling_width
        y = parent.get_center()[1] - self.vertical_spacing
        return [x, y, 0]
     
class OneChildPositioner:
    def __init__(self, vertical_spacing = 1.5):
        self.vertical_spacing = vertical_spacing

    def get_subproblem_position(self, current_subproblem):
        parent = current_subproblem.parent
        if parent is None:
            return [0, 3, 0]

        x = parent.get_center()[0]
        y = parent.get_center()[1] - self.vertical_spacing
        return [x, y, 0]
    