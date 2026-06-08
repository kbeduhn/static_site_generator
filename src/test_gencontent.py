import unittest
from gencontent import extract_title

class TextExtractTitle(unittest.TestCase):
    # A normal h1: "# Hello"
    def test_normal(self):
        markdown = "# Hello world"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello world")

    # An h1 with extra whitespace: "#   Hello world "
    def test_extra_whitespace(self):
        markdown = "#   Hello world  "
        result = extract_title(markdown)
        self.assertEqual(result, "Hello world")

    # An h1 in the middle of a multi-line document
    def test_h1_middle_multi_line(self):
        markdown = "j;lsadjflds\n# Hello world\na;sldkfjdslk"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello world")

    # A document with no h1 (should raise)
    def test_no_h1(self):
        markdown = "## dance ### dance #### revolution"
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
