import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_no_markup(self):
        node = TextNode("This text contains no markups and so should not be processed.", TextType.TEXT)
        new_nodes = [node]
        new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
        expected = [
            TextNode("This text contains no markups and so should not be processed.", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_bold_markup(self):
        node = TextNode("This text contains **bold** markup.", TextType.TEXT)
        new_nodes = [node]
        new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD)
        expected = [
            TextNode("This text contains ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" markup.", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_code_markup(self):
        node = TextNode("This text contains `code` markup.", TextType.TEXT)
        new_nodes = [node]
        new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
        expected = [
            TextNode("This text contains ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" markup.", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_italic_markup(self):
        node = TextNode("This text contains _italic_ markup.", TextType.TEXT)
        new_nodes = [node]
        new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)
        expected = [
            TextNode("This text contains ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" markup.", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_parsing_exception(self):
        node = TextNode("This text contains a _markup error.", TextType.TEXT)
        new_nodes = [node]
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)


    def test_all_delimiters(self):
        node = TextNode("_This_ text contains a mixture of markups, like **bold**, _italic_, and `code`.", TextType.TEXT)
        new_nodes = [node]
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        expected = [
            TextNode("_This_ text contains a mixture of markups, like **bold**, _italic_, and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        expected = [
	        TextNode("_This_ text contains a mixture of markups, like ", TextType.TEXT),
	        TextNode("bold", TextType.BOLD),
	        TextNode(", _italic_, and ", TextType.TEXT),
	        TextNode("code", TextType.CODE),
	        TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        expected = [
	            TextNode("This", TextType.ITALIC),
	            TextNode(" text contains a mixture of markups, like ", TextType.TEXT),
	            TextNode("bold", TextType.BOLD),
	            TextNode(", ", TextType.TEXT),
	            TextNode("italic", TextType.ITALIC),     
	            TextNode(", and ", TextType.TEXT),
	            TextNode("code", TextType.CODE),
	            TextNode(".", TextType.TEXT),
            ]
        self.assertEqual(
            new_nodes,
            expected
        )
        


if __name__ == "__main__":
    unittest.main()   
