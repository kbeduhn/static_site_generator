from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            parts = old_node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception(f"No matching closing delimiter found")

            # Even indices become TEXT nodes
            for i in range(0, len(parts)):
                if i % 2 == 0:
                    node = TextNode(parts[i], TextType.TEXT)
                    new_nodes.append(node)
                # odd indices become text_type nodes.
                else:
                    node = TextNode(parts[i], text_type)
                    new_nodes.append(node)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        remaining_text = old_node.text
        if images == []:
            new_nodes.append(old_node)
            continue
        for image in images:
            alt_text = image[0]
            url = image[1]
            sections = remaining_text.split(f"![{alt_text}]({url})", 1)
            remaining_text = sections[1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        remaining_text = old_node.text
        if links == []:
            new_nodes.append(old_node)
            continue
        for link in links:
            anchor_text = link[0]
            url = link[1]
            sections = remaining_text.split(f"[{anchor_text}]({url})", 1)
            remaining_text = sections[1]
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def test_text_to_textnodes(self):
    nodes = text_to_textnodes("your input string here")
    self.assertListEqual(
        [
            # your expected TextNode list here
        ],
        nodes,
    )

# Other possible tests:
#What if the input has no markdown at all — just plain text?
#What if there's only one type of formatting, like only bold?
#What if the string is empty?





















