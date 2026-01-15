from enum import Enum 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if is_heading_block(block):
        return BlockType.HEADING
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_unordered_list_block(block):
        return BlockType.ULIST
    elif is_ordered_list_block(block):
        return BlockType.OLIST
    elif is_code_block(block):
        return BlockType.CODE
    else:
        return BlockType.PARAGRAPH

def is_heading_block(block):
    if len(block.split('\n')) > 1:
        return False
    
    index = 0
    count = 0
    while index < len(block) and block[index] == '#':
        index += 1
        count += 1

    if count == 0 or count > 6:
        return False
    elif index < len(block) and block[index] == ' ':
        return True
    else:
        return False
    
def is_quote_block(block):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith('> '):
            return False
    return True

def is_unordered_list_block(block):
    lines = block.split('\n')
    for line in lines:
        if not line.startswith('- '):
            return False
    return True

def is_code_block(block):
    lines = block.split('\n')
    if len(lines) > 1 and block[0:4] == '```\n' and block[-3:] == '```':
        return True
    return False

def is_ordered_list_block(block):
    lines = block.split('\n')
    count = 1
    for line in lines:
        expected = f"{str(count)}. "
        if not line.startswith(expected):
            return False
        count += 1
    return True
