LINK_1 = "https://www.google.com"
ANCHOR_1 = "Google"
LINK_2 = "https://www.microsoft.com"
ANCHOR_2 = "Microsoft"

IMAGE_1 = "https://i.imgur.com/zjjcJKZ.png"
ALT_TEXT_1 = "Python Logo"
IMAGE_2 = "https://i.imgur.com/JmwOq9S.jpeg"
ALT_TEXT_2 = "cat"

TEST_TEXT_1 = f"This is text with an image:![{ALT_TEXT_1}]({IMAGE_1}). "
TEST_TEXT_2 = f"This is text with a hyperlink:[{ANCHOR_1}]({LINK_1}). "
TEST_TEXT_3A = f"This text contains two images: ![{ALT_TEXT_1}]({IMAGE_1}) and ![{ALT_TEXT_2}]({IMAGE_2}). "
TEST_TEXT_3B = f"This text contains two hyperlinks: [{ANCHOR_1}]({LINK_1}) and [{ANCHOR_2}]({LINK_2}). "
TEST_TEXT_3 = f"{TEST_TEXT_3A}{TEST_TEXT_3B}"

EXTRACT_IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
EXTRACT_LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
