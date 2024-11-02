from enum import Enum
from htmlnode import *
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
    
    def text_node_to_html_node(self):
        if self.type == TextType[0]:
            node = LeafNode(None,self.text,None)
        elif self.type == TextType[1]:
            node = LeafNode("b",self.text,None)
        elif self.type == TextType[2]:
            node = LeafNode("i",self.text,None)
        elif self.type == TextType[3]:
            node = LeafNode("code",self.text,None)
        elif self.type == TextType[4]:
            node = LeafNode("a",self.text,{"href":self.url})
        elif self.type == TextType[5]:
            node = LeafNode("img",None,{"src": self.url, "alt": self.text})
        else:
            raise ValueError("wrong text enum")
        return node

    
    