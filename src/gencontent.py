from textnode import TextNode
from htmlnode import LeafNode, ParentNode, HTMLNode
from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:]
    raise ValueError("no title found")
    
def generate_page(from_path, template_path, dest_path):
    markdown_file = Path(from_path)
    template = Path(template_path)
    html_file = Path(dest_path)

    print(f"Generating page from {markdown_file} to {html_file} using {template}")

    with markdown_file.open("r") as file:
        markdown = file.read()

    with template.open("r") as file:
        template_file = file.read()

    htmlnode = markdown_to_html_node(markdown)
    html = htmlnode.to_html()

    page_title = extract_title(markdown)

    template_file = template_file.replace("{{ Title }}", page_title)
    template_file = template_file.replace("{{ Content }}", html)

    html_file.parent.mkdir(parents=True, exist_ok=True)
    with html_file.open("w") as file:
        file.write(template_file)

    return

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = Path(dir_path_content)
    template = Path(template_path)
    destination = Path(dest_dir_path)

    for entry in content.iterdir():
        if entry.is_dir():
            next_destination = destination.joinpath(entry.name)
            generate_pages_recursive(entry, template, next_destination)
        elif entry.is_file():
            if entry.suffix == '.md':
                html_file = entry.stem + '.html'
                destination_file = destination.joinpath(html_file)
                generate_page(entry, template, destination_file)
