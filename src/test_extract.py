import unittest
from splitnodes import extract_markdown_images, extract_markdown_links
from test_config import *

class TestHTMLNode(unittest.TestCase):

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