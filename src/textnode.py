from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "text"
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
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT.value:
            return LeafNode(None, text_node.text)
        if text_node.text_type == TextType.BOLD.value:
            return LeafNode("b", text_node.text)
        if text_node.text_type == TextType.ITALIC.value:
            return LeafNode("i", text_node.text)
        if text_node.text_type == TextType.CODE.value:
            return LeafNode("code", text_node.text)
        if text_node.text_type == TextType.LINK.value:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == TextType.IMAGE.value:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"Invalid text type: {text_node.text_type}")
            
    