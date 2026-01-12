import unittest

from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(
            "p", 
            "Hello, world!",
        )
        self.assertEqual(
            node.to_html(), 
            "<p>Hello, world!</p>",
        )

    def test_left_to_html_a(self):
        node = LeafNode(
            "a",
            "Click me!",
            {" href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_values(self):
        node = LeafNode(
            "p", 
            "This is a paragraph of text.",
        )
        self.assertEqual(
            node.tag, 
            "p",
        )
        self.assertEqual(
            node.value,
            "This is a paragraph of text."
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None
        )

        node = LeafNode(
            "a",
            "Click me!",
            '{" href": "https://www.google.com"}'
        )
        self.assertEqual(
            node.tag,
            "a",
        )
        self.assertEqual(
            node.value,
            "Click me!",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            '{" href": "https://www.google.com"}'
        )



if __name__ == "__main__":
    unittest.main()    