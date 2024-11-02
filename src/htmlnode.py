from textnode import *
class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.val = value
        self.children = children
        self.props = props
    

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        if self.props is not None:
           for thing in self.props:
                result += f' {thing}="{self.props[thing]}"'
        return result
    
    def __repr__(self):
        return f"tag = {self.tag} value = {self.val} childred= {self.children} props = {self.props}"
        

class LeafNode(HTMLNode):
    def __init__(self,tag,value, props=None):
        super().__init__()
        self.tag = tag
        self.val = value
        self.props = props
        
    def to_html(self):
        if self.val == None:
            raise ValueError()
        if self.tag == None:
            return self.val
        return f"<{self.tag}{self.props_to_html()}>{self.val}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        if self.children == None:
            raise ValueError("no child")
        final = ""
        check = []
        if type(self.children) != type(check):
            self.children = [self.children]
        for child in self.children:
            final += child.to_html()
        
        return "<p>"+final+"</p>"

        