import re
from textnode import TextNode, TextType

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0: # a missing matching closing delimiter will produce an even number of split parts
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            # evenly indexed parts will be plain text
            if sections[i] == "":
                # empty text node, so don't include it
                continue
            if i % 2 == 0:
                # even nodes are non-markdown text
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                # odd nodes are markdown text
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        current_text = old_node.text
        images = extract_markdown_images(current_text)
        if not images:
            new_nodes.append(old_node)
            continue

        for image in images:
            # build the markdown string
            image_alt, image_link = image
            markdown = f"![{image_alt}]({image_link})"

            # now split current_text using the markdown
            # as the delimiter
            sections = current_text.split(markdown, 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            
            # if the left section is not an empty string,
            # turn it into a TextType.TEXT node and append 
            # it to list of nodes to return
            if sections[0] != "":
                textnode = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(textnode)

            # now create a TypeText.IMAGE node and append it
            # to the list of nodes to return
            link_node = TextNode(image_alt, TextType.IMAGE, image_link)
            new_nodes.append(link_node)

            # set current_text to the right section 
            current_text = sections[1]
        if current_text != "":
            textnode = TextNode(current_text, TextType.TEXT)
            new_nodes.append(textnode)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        current_text = old_node.text
        links = extract_markdown_links(current_text)
        if not links:
            new_nodes.append(old_node)
            continue
        for link in links:
            # build the markdown string
            link_anchor, link_url = link
            markdown = f"[{link_anchor}]({link_url})"

            # now split current_text using the markdown
            # as the delimiter
            sections = current_text.split(markdown, 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            
            # if the left section is not an empty string,
            # turn it into a TextType.TEXT node and append 
            # it to list of nodes to return
            if sections[0] != "":
                textnode = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(textnode)

            # now create a TypeText.LINK node and append it
            # to the list of nodes to return
            linknode = TextNode(link_anchor, TextType.LINK, link_url)
            new_nodes.append(linknode)

            # set current_text to the right section 
            current_text = sections[1]
        if current_text != "":
            textnode = TextNode(current_text, TextType.TEXT)
            new_nodes.append(textnode)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

