from textnode import TextType
from htmlnode import LeafNode, ParentNode, HTMLNode
from inline_markdown import *
from markdown_blocks import markdown_to_html_node
from pprint import pprint



def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(node)

    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    print(node.to_html())

#main()