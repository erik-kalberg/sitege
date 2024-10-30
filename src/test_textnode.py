import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eqf(self):
        node = TextNode("This is a text node", TextType.BOLD , url = None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_types(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a text node", TextType.CODE ,  "test")
        node2 = TextNode("This is a text node", TextType.CODE , "test")
        self.assertEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()