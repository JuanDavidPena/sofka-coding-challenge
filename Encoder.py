from json import JSONEncoder

class Encoder(JSONEncoder):
    """Encoder class that encodes objects to json"""
    def default(self, o):
        return o.__dict__

