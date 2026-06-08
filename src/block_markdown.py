from enum import Enum

def markdown_to_blocks(markdown):
    line_spacing = markdown.split("\n\n")
    result = []
    for block in line_spacing:
        cleaned = block.strip()
        if cleaned != "":
            result.append(cleaned)
    return result

# block_type
class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block):
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.heading

    # Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.code

    # Every line in a quote block must start with a "greater-than" character: > followed by the quote text.
    # A space after > is allowed but not required.
    if block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return block_type.paragraph
        return BlockType.quote

    # Every line in an unordered list block must start with a - character, followed by a space.
    if block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith("- "):
                return block_type.paragraph
        return BlockType.unordered_list

    # Every line in an ordered list block must start with a number followed by a . character and a space.
    # The number must start at 1 and increment by 1 for each line.
    if block.startswith("1. "):
        lines = block.split("\n")
        count = 1
        for line in lines:
            if line.startswith(f"{count}. "):
                count += 1
            else:
                return block_type.paragraph
        return BlockType.ordered_list

    # If none of the above conditions are met, the block is a normal paragraph.
    return BlockType.paragraph
