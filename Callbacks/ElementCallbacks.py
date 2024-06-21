from manim import *

class Callback:

    def on_create(self, element):
        return Wait(0.1)

    def on_delete(self, element):
        return Wait(0.1)

    def before_set_data(self, element):
        return Wait(0.1)

    def after_set_data(self, element):
        return Wait(0.1)

    def before_set_style(self, element):
        return Wait(0.1)

    def after_set_style(self, element):
        return Wait(0.1)
    
    def on_visit_start(self, element):
        return Wait(0.1)

    def on_visit_end(self, element):
        return Wait(0.1)


class zoomToElementCallback(Callback):
    def __init__(self, camera, zoom_factor=14):
        super().__init__()
        self.camera = camera
        self.zoom_factor = zoom_factor

    def on_visit_start(self, element):
        return self.camera.frame.animate.move_to(element).set(width=min(element.get_width(), element.get_height()) * self.zoom_factor)

    def on_visit_end(self, element):
        return self.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width)


class displayCodeRecursionCallback(Callback):
    def __init__(self, code_window, display_indices, orientation=LEFT):
        super().__init__()
        self._num_visited_subarrays = 0
        self.code_window = code_window
        self.display_indices = display_indices
        self.orientation = orientation
  
    def on_visit_start(self, recursion):
        if self._num_visited_subarrays in self.display_indices:
            self.code_window.code.next_to(recursion.current_subproblem, self.orientation)
            return AnimationGroup(self.code_window.animate.set_opacity(1))
        return Wait(0.1)
    
    def on_visit_end(self, recursion):
        self._num_visited_subarrays += 1
        return self.code_window.animate.set_opacity(0)

class displayCodeElementCallback(Callback):
    def __init__(self, code_window, orientation=LEFT):
        super().__init__()
        self._num_visited_subarrays = 0
        self.code_window = code_window
        self.orientation = orientation
  
    def on_visit_start(self, element):
        self.code_window.code.next_to(element, self.orientation)
        return AnimationGroup(self.code_window.animate.set_opacity(1))
    
    def on_visit_end(self, element):
        self._num_visited_subarrays += 1
        return self.code_window.animate.set_opacity(0)
    
class zoomToRecursionCallback(Callback):
    def __init__(self, scene, display_indices, zoom_factor):
        super().__init__()
        self.scene = scene
        self._num_visited_subarrays = 0
        self.display_indices = display_indices
        self.zoom_factor = zoom_factor
  
    def on_visit_start(self, recursion):
        if self._num_visited_subarrays in self.display_indices:
            return self.scene.camera.frame.animate.move_to(recursion.current_subproblem).set(width=min(recursion.current_subproblem.get_width(), recursion.current_subproblem.get_height()) * self.zoom_factor)
        return Wait(0.1)
    
    def on_visit_end(self, recursion):
        self._num_visited_subarrays += 1
        return self.scene.camera.frame.animate.move_to(ORIGIN).set(width=config.frame_width)
