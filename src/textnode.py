from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
class TextNode():
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = None
        self.url = url
        for kind in TextType:
            if kind == type:
                self.type = kind.value 
    def __eq__(self, other):
        if self.text == other.text:
            if self.type == other.type:
                if self.url == other.url:
                    return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type}, {self.url})"