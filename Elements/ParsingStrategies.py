from abc import ABC, abstractmethod

"""
Provides classes that convert an element's data for compatability with the manim Text object
For all implementations:

func parse: Converts a raw data type to a string to use with Text(str)
func invert_parse: Converts Text.text to original type for comparison
"""

class AbstractParser(ABC):
    @abstractmethod
    def parse(self, data):
        pass

    @abstractmethod
    def invert_parse(self, data_str):
        pass

    def _check_is_string(self, data_str):
        if not isinstance(data_str, str):
            raise TypeError(f"AbstractParser.invert_parse expects a string, got: {type(data_str)}")

class IntParser(AbstractParser):
    def parse(self, data):
        if not isinstance(data, int):
            raise TypeError(f"IntParser got data type: {type(data)}")
        return str(data)
    
    def invert_parse(self, data_str):
        self._check_is_string(data_str)
        return int(data_str)
    
class DictParser(AbstractParser):
    def parse(self, data):
        if not isinstance(data, dict):
            raise TypeError(f"DictParser got data type : {type(data)}")
        combined_str = ""
        for key in data.keys():
            combined_str += str(key) + " = " + str(data[key]) + "\n"
        return combined_str

    def invert_parse(self, data_str):
        self._check_is_string(data_str)
        data_dict = {}
        lines = data_str.split("\n")
        for line in lines:
            key, value = line.split(" = ")
            data_dict[key.strip()] = value.strip()
        return data_dict

class StringParser(AbstractParser):
    def parse(self, data):
        if not isinstance(data, str):
            raise TypeError(f"StringParser got data type: {type(data)}")
        return data
    
    def invert_parse(self, data_str):
        self._check_is_string(data_str)
        return data_str
    