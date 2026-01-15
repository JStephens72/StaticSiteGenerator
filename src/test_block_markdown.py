import unittest
from markdown_blocks import (
    markdown_to_blocks,
    is_heading_block,
    is_quote_block,
    is_unordered_list_block,
    is_ordered_list_block,
    is_code_block,
    block_to_block_type,
    BlockType
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is a **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                'This is a **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items',
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_block_type_heading(self):
        block = '# Heading 1'
        self.assertTrue(is_heading_block(block))

        block = '## Heading 1'
        self.assertTrue(is_heading_block(block))

        block = '### Heading 1'
        self.assertTrue(is_heading_block(block))

        block = '#### Heading 1'
        self.assertTrue(is_heading_block(block))

        block = '##### Heading 1'
        self.assertTrue(is_heading_block(block))

        block = '###### Heading 1'
        self.assertTrue(is_heading_block(block))

        block = '####### Heading 1'
        self.assertFalse(is_heading_block(block))

        block = '#Heading 1'
        self.assertFalse(is_heading_block(block))

        block = '# Heading 1\n# Make it multine.'
        self.assertFalse(is_heading_block(block))

        block = '<h1>Heading 1</h1>'
        self.assertFalse(is_heading_block(block))

        block = '''> quote 1
> quote 2
> quote 3'''
        self.assertTrue(is_quote_block(block))

        block = '''>quote 1
>quote 2
>quote 3'''
        self.assertFalse(is_quote_block(block))

        block = '''>quote 1
quote 2
>quote 3'''
        self.assertFalse(is_quote_block(block))

        block = '''- item 1
- item 2
- item 3'''
        self.assertTrue(is_unordered_list_block(block))

        block = '''- item 1
- item 2
- item 3
'''
        self.assertFalse(is_unordered_list_block(block))

        block = '''
- item 1
- item 2
- item 3'''
        self.assertFalse(is_unordered_list_block(block))

        block = '''- item 1
-item 2
- item 3'''
        self.assertFalse(is_unordered_list_block(block))

        block = '''1. item 1
2. item 2
3. item 3'''
        self.assertTrue(is_ordered_list_block(block))

        block = '''1. item 1
1. item 2
1. item 3'''
        self.assertFalse(is_ordered_list_block(block))

        block = '''1.item 1
2.item 2
3.item 3'''
        self.assertFalse(is_ordered_list_block(block))

        block = '''```
line 1
line 2```'''
        self.assertTrue(is_code_block(block))

        block = '''```line 1
line 2```
'''
        self.assertFalse(is_code_block(block))

    def test_block_to_block_type(self):
        block = '''#### Heading 4'''
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

if __name__ == "__main__":
    unittest.main()   
