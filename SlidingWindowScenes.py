from manim import *
from SlidingWindow import SlidingWindow
from CodeWindow import CodeWindow

class SlidingWindowScene(Scene):
    def __init__(self, data, code_file, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = "#2A2B2E"
        self.data = data
        self.code_file = code_file

    def construct(self):
        code_window = CodeWindow(self, self.code_file)
        sliding_window = SlidingWindow(self.data, self)

        self.play(Create(sliding_window.array_visual), Write(code_window.code))
        self.wait(1)

        self.run(sliding_window, code_window)

    def run(self, sliding_window, code_window):
        pass

class MaxProfitScene(SlidingWindowScene):
    def run(self, sliding_window:SlidingWindow, code_window:CodeWindow):
        prices = self.data
        i = 0
        j = 0
        sliding_window.initialize_pointers()
        max_profit = 0
        sliding_window.display_custom_variable("Max Profit", max_profit)

        while j < len(prices):
            sliding_window.update_j_pointer(j)
            code_window.highlight_line(4, run_time=0.2)
            code_window.highlight_line(5)
            if prices[j] < prices[i]:
                code_window.highlight_line(6)
                i = j
                sliding_window.update_i_pointer(i)
            else:
                code_window.highlight_line(7, run_time=0.2)
                code_window.highlight_line(8)
                sliding_window.display_custom_variable("Max Profit", f"Max({max_profit}, {prices[j]} - {prices[i]})")
                max_profit = max(max_profit, (prices[j] - prices[i]))
                sliding_window.display_custom_variable("Max Profit", max_profit)
            self.wait(0.1)
            j += 1
            code_window.highlight_line(9)
        code_window.highlight_line(10)

class UniqueSubstringScene(SlidingWindowScene):
    def run(self, sliding_window:SlidingWindow, code_window:CodeWindow):
        s = self.data
        i = 0
        j = 0
        sliding_window.initialize_pointers()
        longest_substring = 0
        sliding_window.display_custom_variable("Longest Substring", longest_substring)

        while j < len(s):
            sliding_window.update_j_pointer(j)
            code_window.highlight_line(4, 0.2)
            code_window.highlight_line(5)
            if s[j] in s[i:j]:
                code_window.highlight_line(6)
                duplicate_index = s.index(s[j])
                sliding_window.display_i_j_comparison(duplicate_index,j)
                self.wait(0.2)
                i += 1
                sliding_window.update_i_pointer(i)
                sliding_window.display_window_box(i,j-1)
            else:
                code_window.highlight_line(7, 0.2)
                code_window.highlight_line(8)
                sliding_window.display_custom_variable("Longest Substring", f"Max{longest_substring}, {j} - {i} + 1)")
                longest_substring = max(longest_substring, j - i + 1)
                sliding_window.display_custom_variable("Longest Substring", longest_substring)
                code_window.highlight_line(9)
                sliding_window.display_window_box(i,j)
                j += 1

        code_window.highlight_line(10)
        