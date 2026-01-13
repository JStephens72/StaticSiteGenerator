from textnode import TextNode, TextType
from htmlnode import LeafNode
import re
from config import *

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(text_node)

    text = TEST_TEXT_1
    print(extract_markdown_images(text))
    
    text = TEST_TEXT_2
    print(extract_markdown_links(text))
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        
        case TextType.LINK:
            props = {"href": text_node.url}
            return LeafNode("a", text_node.text, props)
        
        case TextType.IMAGE:
            props = {
                "src": text_node.url,
                "alt": text_node.text,
            }

            return LeafNode("img", "", props )
        
        case _:
            raise ValueError(f"Error: {text_node.text_type} is not a valid TextType")
        
def extract_markdown_images(text):
    matches = re.findall(EXTRACT_IMAGE_REGEX, text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(EXTRACT_LINK_REGEX, text)
    return matches

def split_nodes_image(old_nodes):
    pass

def split_nodes_links(old_nodes):
    pass

#main()