import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None,None,None,{
        "href": "https://www.google.com", 
        "target": "_blank",
        })
        string =  ' href="https://www.google.com" target="_blank"'
        test = node.props_to_html()
        self.assertEqual(test, string)

    def test_simple_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.")
        test = node.to_html()
        string = "<p>This is a paragraph of text.</p>"
        self.assertEqual(test,string)

    def test_leaf_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        test = node.to_html()
        string = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(test,string)

    def test_parent_dink(self):
        node = ParentNode("p",None)
        self.assertRaises(ValueError,node.to_html)

    def test_catholic_parent(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
        )

        test = node.to_html()
        compare = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(test,compare)

    def test_full_nester(self):
        node_one = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
            )
        
        node_two = ParentNode(
        "p",
        [
            
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
            )
        test_node = ParentNode("p",[node_one,node_two],)
        test= test_node.to_html()
        string = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
        self.assertEqual(test,string)
    def test_single_child(self):
        node = LeafNode("a", "This is a paragraph of text.")
        parent = ParentNode("p",node,None)
        test = parent.to_html()
        string = "<p><a>This is a paragraph of text.</a></p>"
        self.assertEqual(test,string)