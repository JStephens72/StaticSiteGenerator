from textnode import TextNode
from textnode import TextType
from pprint import pprint

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

