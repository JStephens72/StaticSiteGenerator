import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_child_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            f"<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
        )

    def test_values(self):
        list_children = [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        node = ParentNode(
            "p",
            list_children,
        )
        self.assertEqual(
            node.tag,
            "p",
        )
        self.assertEqual(
            node.value,
            None,
        )
        self.assertEqual(
            node.children,
            list_children,
        )
        self.assertEqual(
            node.props,
            None
        )



if __name__ == "__main__":
    unittest.main()    