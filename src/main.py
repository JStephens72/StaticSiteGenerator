from textnode import TextType
from htmlnode import LeafNode
from inline_markdown import *
from block_markdown import markdown_to_blocks
from pprint import pprint


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()