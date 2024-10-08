from manim import *
from Elements.Element import Element
import numpy as np

#TODO
class GraphElement(Element):
    def __init__(self, data, shape=Square, style={Square:{}, Text:{}}, callbacks=[], **kwargs):
        super().__init__(data, shape, style, callbacks, **kwargs)
        # Contains (Element, weight) tuples or just Element for unweighted graph?
        self.incoming_edges = []
        self.outgoing_edges = []

    def add_incoming_edge(self, new_edge):
        self.incoming_edges.append(new_edge)
    
    def add_outgoing_edge(self, new_edge):
        self.outgoing_edges.append(new_edge)
        print(new_edge)
        start_pt, end_pt = self._get_arrow_start_end_coordinates(self, new_edge[0]) 
        new_arrow = CurvedArrow(start_pt, end_pt)
        
        direction = self._nudge_edge_weight(new_arrow)
        edge_weight = Text(str(new_edge[1]), font_size=24).next_to(new_arrow.get_midpoint(), direction)
        edge_animation = FadeIn(edge_weight) 
            
        self.add(new_arrow)
        return AnimationGroup(edge_animation, FadeIn(new_arrow))
    
    def _nudge_edge_weight(self, arrow):
        # Is the arrow drawn vertically? Nudge left. Is it drawn horizontally? Nudge down
        start = arrow.get_start()
        end = arrow.get_end()
        diff = start - end
        if abs(diff[0]) > abs(diff[1]):
            return DOWN
        return LEFT
        
    
    def _get_arrow_start_end_coordinates(self, origin, destination):
        #print(f"Got shape locations: {origin_shape.get_center()} and {destination_shape.get_center()}")
        midpoint = (origin.shape.get_center() + destination.shape.get_center()) / 2

        def get_min_euc_dist(shape, point):
            def euc_dist(point1, point2):
                return np.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
            
            left_dist = euc_dist(shape.get_left(), point)
            right_dist = euc_dist(shape.get_right(), point)
            top_dist = euc_dist(shape.get_top(), point)
            bottom_dist = euc_dist(shape.get_bottom(), point)
            min_dist = min(left_dist, right_dist, top_dist, bottom_dist)

            if min_dist == left_dist:
                return shape.get_left()
            elif min_dist == right_dist:
                return shape.get_right()
            elif min_dist == top_dist:
                return shape.get_top()
            else:
                return shape.get_bottom()
            
        return get_min_euc_dist(origin.shape, midpoint), get_min_euc_dist(destination.shape, midpoint)


    def create(self):
        return AnimationGroup(FadeIn(self.shape), FadeIn(self.data))
    
    def delete(self):
        return FadeOut(self)