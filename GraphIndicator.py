from manim import *
import warnings

class GraphIndicator(VGroup):
    def __init__(self, graph, shape, style, **kwargs):
        super().__init__(**kwargs)
        self.graph = graph
        self.style = style
        self.shape = type(shape)(**self.style[type(shape)])
        self.add(self.shape)
        self.current_node = None
        
    def visit(self, new_node):
        # if self._is_valid_visit(new_node) == False:
        #     warnings.warn("Graph Indicator tried to visit node with nonexistent edge")
        #     return Wait(0)
        #move_to should move along the arrow's curve
        self.current_node = new_node
        return self.animate.move_to(self.current_node.shape)
    
    def _is_valid_visit(self, new_node):
        for e in self.graph.edges:
            if id(e[0]) == id(self.current_node) and id(e[1]) == id(new_node):
                return True
        return False
        
    def create(self, node):
        self.current_node = node
        self.shape.move_to(node.shape.get_center())
        return FadeIn(self)
    
    
    
        
        
    