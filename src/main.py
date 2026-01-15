from textnode import TextType
from htmlnode import LeafNode
from inline_markdown import *
from markdown_blocks import *
from pprint import pprint


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()