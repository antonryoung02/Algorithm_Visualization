from SlidingWindowScenes import MaxProfitScene, UniqueSubstringScene

prices = [6, 4, 5, 2, 7, 8, 1]
code_file = "maxprofitcode.py"

class MyMaxProfitScene(MaxProfitScene):
    def __init__(self):
        super().__init__(prices, code_file)

s = "dflefea"
code_file = "longestuniquesubstring.py"

class MyUniqueSubstringScene(UniqueSubstringScene):
    def __init__(self):
        super().__init__(s, code_file)