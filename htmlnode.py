
class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.val = value
        self.children = children
        self.props = props
    

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        for thing in self.props:
            result += f" h{thing}= {self.props[thing]}"
        return result
    
    def __repr__(self):
        print(f"tag = {self.tag} value = {self.val} childred= {self.children} props = {self.props}")
        return

