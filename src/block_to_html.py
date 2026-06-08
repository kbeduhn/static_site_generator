from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes
from htmlnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.heading:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            tag = f"h{level}"
            text = block[level + 1:]
            children = text_to_children(text)
            heading_node = ParentNode(tag, children)
            block_nodes.append(heading_node)

        elif block_type == BlockType.code:
            inner_text = block[4:-3]
            raw_text_node = TextNode(inner_text, TextType.TEXT)
            code_child = text_node_to_html_node(raw_text_node)
            code_node = ParentNode("code", [code_child])
            pre_node = ParentNode("pre", [code_node])
            block_nodes.append(pre_node)

        elif block_type == BlockType.quote:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                cleaned = line.lstrip(">").strip()
                new_lines.append(cleaned)
            text = " ".join(new_lines)
            children = text_to_children(text)
            quote_node = ParentNode("blockquote", children)
            block_nodes.append(quote_node)

        elif block_type == BlockType.unordered_list:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                text = line[2:]
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            ul_node = ParentNode("ul", li_nodes)
            block_nodes.append(ul_node)

        elif block_type == BlockType.ordered_list:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                text = line[3:]
                children = text_to_children(text)
                li_nodes.append(ParentNode("li", children))
            ol_node = ParentNode("ol", li_nodes)
            block_nodes.append(ol_node)

        elif block_type == BlockType.paragraph:
            text = " ".join(block.split("\n"))
            children = text_to_children(text)
            paragraph_node = ParentNode("p", children)
            block_nodes.append(paragraph_node)

    return ParentNode("div", block_nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

