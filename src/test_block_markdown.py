def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

import unittest
from block_markdown import block_to_block_type, BlockType

class TestMarkdownBlocks(unittest.TestCase):
    def test_heading(self):
        result = block_to_block_type("## Life, um, finds a way")
        self.assertEqual(result, BlockType.heading)

    def test_code(self):
        result = block_to_block_type("```\nthen it doesn't really\nmatter which way you go\n```")
        self.assertEqual(result, BlockType.code)

    def test_quote(self):
        result = block_to_block_type("> nah nah nah nah nah nah nah nah hey, hey, hey, goodbye")
        self.assertEqual(result, BlockType.quote)

    def test_unordered_list(self):
        result = block_to_block_type("- Oogum, oogum, boogum, boogum, boogum, now, baby, you're casting your spell on me")
        self.assertEqual(result, BlockType.unordered_list)

    def test_ordered_list(self):
        result = block_to_block_type("1. damn it feels good to be a gangsta\n2. a gangsta ass n**** play his cards right")
        self.assertEqual(result, BlockType.ordered_list)

    def test_paragraph(self):
        result = block_to_block_type("Sweet Caroline buh buh buh")
        self.assertEqual(result, BlockType.paragraph)
