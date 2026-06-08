import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is another text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("yet another text node", TextType.TEXT)
        node2 = TextNode("yet another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_3(self):
        node = TextNode("test node", TextType.LINK)
        node2 = TextNode("test node", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    if __name__  == "__main__":
        unittest.main()

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_text_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_text_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_text_link(self):
        node = TextNode("click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value, "click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_text_image(self):
        node = TextNode("imag", TextType.IMAGE, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com", "alt": "imag"})

    def text_invalid(self):
        node = TextNode("oops", "invalid_type")
        self.assertRaises(Exception, text_node_to_html_node, node)









