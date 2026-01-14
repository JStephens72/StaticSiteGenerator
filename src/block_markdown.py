def markdown_to_blocks(document):
    blocks = []
    temp_blocks = document.split("\n\n")
    for i in range(len(temp_blocks)):
        if len(temp_blocks[i].strip()) == 0:
            continue
        blocks.append(temp_blocks[i].strip())
    return blocks
