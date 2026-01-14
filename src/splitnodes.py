from textnode import TextNode
from textnode import TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_values = node.text.split(delimiter)
            if len(split_values) % 2 != 1: # a missing matching closing delimiter will produce an even number of split parts
                raise ValueError("Error: Missing closing delimiter")
            for i in range(0, len(split_values), 2):
                # evenly indexed parts will be plain text
                if split_values[i] != "":
                    new_nodes.append(TextNode(split_values[i], TextType.TEXT))
                if i != (len(split_values) - 1) and split_values[i + 1] != "":
                    new_nodes.append(TextNode(split_values[i + 1], text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        matches = extract_markdown_images(current_text)

        if not matches:
            new_nodes.append(node)
            continue

        for match in matches:
            # build the markdown string
            image_alt, image_link = match
            markdown = f"![{image_alt}]({image_link})"

            # now split current_text using the markdown
            # as the delimiter
            sections = current_text.split(markdown, 1)
            
            # if the left section is not an empty string,
            # turn it into a TextType.TEXT node and append 
            # it to list of nodes to return
            if not sections[0] == "":
                textnode = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(textnode)

            # now create a TypeText.IMAGE node and append it
            # to the list of nodes to return
            linknode = TextNode(image_alt, TextType.IMAGE, image_link)
            new_nodes.append(linknode)

            # set current_text to the right section 
            current_text = sections[1]

        if current_text != "":
            textnode = TextNode(current_text, TextType.TEXT)
            new_nodes.append(textnode)
        
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        matches = extract_markdown_links(current_text)

        if not matches:
            new_nodes.append(node)
            continue

        for match in matches:
            # build the markdown string
            link_anchor, link_url = match
            markdown = f"[{link_anchor}]({link_url})"

            # now split current_text using the markdown
            # as the delimiter
            sections = current_text.split(markdown, 1)
            
            # if the left section is not an empty string,
            # turn it into a TextType.TEXT node and append 
            # it to list of nodes to return
            if not sections[0] == "":
                textnode = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(textnode)

            # now create a TypeText.LINK node and append it
            # to the list of nodes to return
            imagenode = TextNode(link_anchor, TextType.LINK, link_url)
            new_nodes.append(imagenode)

            # set current_text to the right section 
            current_text = sections[1]

        if current_text != "":
            textnode = TextNode(current_text, TextType.TEXT)
            new_nodes.append(textnode)
        
    return new_nodes
