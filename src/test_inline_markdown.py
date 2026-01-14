import unittest

from inline_markdown import (
    split_nodes_delimiter, 
    split_nodes_link, 
    split_nodes_image, 
    text_to_textnodes,
    extract_markdown_images,
    extract_markdown_links,
)
from textnode import TextNode, TextType
from test_config import *
from pprint import pprint


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

    def test_split_nodes_link_no_link(self):
        node = TextNode(TEST_TEXT_5, TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_link(old_nodes)
        expected = old_nodes
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_split_nodes_link_one_link(self):
        node = TextNode(TEST_TEXT_2, TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_link(old_nodes)
        expected = [
            TextNode("This is text with a hyperlink:", TextType.TEXT),
            TextNode(ANCHOR_1, TextType.LINK, LINK_1),
            TextNode(". ", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_split_nodes_link_two_link(self):
        node = TextNode(TEST_TEXT_3B, TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_link(old_nodes)
        expected = [
            TextNode("This text contains two hyperlinks:", TextType.TEXT),
            TextNode(ANCHOR_1, TextType.LINK, LINK_1),
            TextNode(" and ", TextType.TEXT),
            TextNode(ANCHOR_2, TextType.LINK, LINK_2),
            TextNode(". ", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_split_nodes_image_no_image(self):
        node = TextNode(TEST_TEXT_4, TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_image(old_nodes)
        expected = old_nodes
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_split_nodes_image_one_image(self):
        node = TextNode(TEST_TEXT_1, TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_image(old_nodes)
        expected = [
            TextNode("This is text with an image:", TextType.TEXT),
            TextNode(ALT_TEXT_1, TextType.IMAGE, IMAGE_1),
            TextNode(". ", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_split_nodes_image_two_image(self):
        node = TextNode(TEST_TEXT_3A, TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_image(old_nodes)
        expected = [
            TextNode("This text contains two images:", TextType.TEXT),
            TextNode(ALT_TEXT_1, TextType.IMAGE, IMAGE_1),
            TextNode(" and ", TextType.TEXT),
            TextNode(ALT_TEXT_2, TextType.IMAGE, IMAGE_2),
            TextNode(". ", TextType.TEXT),
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_split_nodes_image_and_link(self):
        node = TextNode(TEST_TEXT_3, TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_link(old_nodes)
        new_nodes = split_nodes_image(new_nodes)
        expected = [
            TextNode("This text contains two images:", TextType.TEXT),
            TextNode(ALT_TEXT_1, TextType.IMAGE, IMAGE_1),
            TextNode(" and ", TextType.TEXT),
            TextNode(ALT_TEXT_2, TextType.IMAGE, IMAGE_2),
            TextNode(". This text contains two hyperlinks:", TextType.TEXT),
            TextNode(ANCHOR_1, TextType.LINK, LINK_1),
            TextNode(" and ", TextType.TEXT),
            TextNode(ANCHOR_2, TextType.LINK, LINK_2),
            TextNode(". ", TextType.TEXT),
            
        ]
        self.assertEqual(
            new_nodes,
            expected
        )

    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(
            nodes,
            expected
        )

class TestImageAndLinkExtract(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            TEST_TEXT_1
        )
        self.assertListEqual([("Python Logo", "https://i.imgur.com/zjjcJKZ.png")], matches)
	
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            TEST_TEXT_2
        )
        self.assertListEqual([("Google", "https://www.google.com")], matches)
	
    def test_extracting_images_and_links(self):
        image_matches = extract_markdown_images(
            TEST_TEXT_3
        )
        self.assertListEqual([("Python Logo", "https://i.imgur.com/zjjcJKZ.png"), ("cat", "https://i.imgur.com/JmwOq9S.jpeg")], image_matches)
        link_matches = extract_markdown_links(
		    TEST_TEXT_3
	    )
        self.assertListEqual([("Google", "https://www.google.com"), ("Microsoft", "https://www.microsoft.com")], link_matches)

        


if __name__ == "__main__":
    unittest.main()   
