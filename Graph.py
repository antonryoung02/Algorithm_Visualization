from manim import AnimationGroup, VGroup

class Graph(VGroup):
    def __init__(self, graph_elements, edges, element_positions=None, **kwargs):
        super().__init__(**kwargs)
        self.elements = graph_elements
        self.edges = edges
        self.element_positions = element_positions

    def create(self):
        for index, element in enumerate(self.elements):
            element.move_to(self.element_positions[index])

        for edge in self.edges:
            origin_element, destination_element, weight = edge
            origin_element.add_outgoing_edge((destination_element, weight))
            destination_element.add_incoming_edge((origin_element, weight))

        return AnimationGroup(*[element.create() for element in self.elements])
    
    def add_element(self, new_element, new_element_position):
        self.elements.append(new_element)
        self.element_positions.append(new_element_position)
        new_element.move_to(new_element_position)
        return new_element.create()

    def add_edge(self, new_edge):
        self.edges.append(new_edge)
        origin_element, destination_element, weight = new_edge
        destination_element.add_incoming_edge((origin_element, weight))
        return origin_element.add_outgoing_edge((destination_element, weight))

