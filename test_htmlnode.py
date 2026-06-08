import unittest

# Test class HTMLNode()
def test_no_props(self):
    node = HTMLNode("p", "Hey, boy, heeey", None, None)
    self.assertEqual(node.props_to_html(), "")

def test_empty_props(self):
    node = HTMLNode("a", "Tell your cat I said hi", None, {})
    self.assertEqual("", {})

def test_standard_input(self):
    node = HTMLNode("b", "Hello", None, {"href": "https://www.google.com"})
    self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

# Test to_html method on HTMLNode() class
def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_no_value(self):
    node = LeafNode("b", None)
    with self.assertRaises(ValueError):
        node.to_html()

def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Hey")
    self.assertEqual(node.to_html(), "Hey")

def test_leaf_to_html_render_tag(self):
    node = LeafNode("a", "Hello", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello</a>')

# Test class ParentNode(HTMLNode)
def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

    #edge case: nesting ParentNode objects inside one another
def test_to_html_with_nested_objects(self):
    great_grandchild = LeafNode("b", "hello")
    grandchild = ParentNode("b", [great_grandchild])
    child = ParentNode("div", [grandchild])
    parent = ParentNode("span", [child])
    self.assertEqual(parent.to_html(), "<span><div><b><b>hello</b></b></div></span>")







