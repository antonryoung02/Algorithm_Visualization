from Elements.ParsingStrategies import DictParser, IntParser, StringParser

class ParserFactory():
    def create_parser(self, data):
        if isinstance(data, dict):
            return DictParser()
        elif isinstance(data, int):
            return IntParser()
        elif isinstance(data, str):
            return StringParser()
        else:
            raise ValueError(f"Unsupported data type: {type(data)}")
        
