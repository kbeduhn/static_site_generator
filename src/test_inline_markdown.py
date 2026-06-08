import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestInlineMarkdown(unittest.TestCase):
    # A test node with a code block
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    # A TEXT node with a bold (** delimiter)
    def test_bold(self):
        node = TextNode("This is text with a **bold** delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" delimiter", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    if __name__ == "__main__":
        unittest.main()

# Split Images and Links Tests
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with [click here](https://google.com) and [olo](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("click here", TextType.LINK, "https://google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("olo", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"
            ),
        ],
        new_nodes,
    )

def test_text_to_textnodes(self):
    new_nodes = text_to_textnodes("This is **text** with _italic font_ and `code block` [link](https://google.com) and ![images](https://i.imgur.com/zjjcJKZ.png)")
    self.assertListEqual(new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with ", TextType.TEXT),
                TextNode("italic font", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("images", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ]
        )

def test_text_to_textnodes(self):
    nodes = text_to_textnodes("your input string here")
    self.assertListEqual(
        [
            # your expected TextNode list here
        ],
        nodes,
    )
