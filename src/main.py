import os
import shutil
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive
from pathlib import Path

STATIC = 'static'
PUBLIC = 'public'
SOURCE = 'content'
TEMPLATE = 'template.html'
DESTINATION = 'public'

def main():

    copy_files_recursive(STATIC, PUBLIC)
    generate_pages_recursive(SOURCE, TEMPLATE, DESTINATION)
    return

main()