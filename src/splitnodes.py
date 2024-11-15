from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for node in old_nodes:
        if node.type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            sentence = node.text
            sentence.split(delimiter)
            if len(sentence)%2 != 1:
                raise Exception("invalid markdown")
            for i in range(0,len(sentence)):
                if i % 2 == 0:
                    new = TextNode(sentence[i],TextType.TEXT)
                    new_nodes.append(new)
                elif i % 2 == 1:
                    new = TextNode(sentence[i],text_type)
                    new_nodes.append(new)


        
        
