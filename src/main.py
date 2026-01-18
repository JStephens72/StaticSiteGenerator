from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive
import sys
from urllib.parse import urlparse

STATIC = 'static'
PUBLIC = 'docs'
SOURCE = 'content'
TEMPLATE = 'template.html'
DESTINATION = 'docs'

def main(basepath):
    

    copy_files_recursive(STATIC, PUBLIC)
    generate_pages_recursive(SOURCE, TEMPLATE, DESTINATION, basepath)
    return

basepath = '/'
print(basepath)
print(len(sys.argv))
if len(sys.argv) == 2:
    basepath = sys.argv[1]
    print(basepath)
    parsed = urlparse(basepath)
    print(parsed.scheme)
    if not (parsed.scheme == 'http' or parsed.scheme == 'https'):
        print("error: url must include http or https")
        sys.exit(1)
    if not parsed.netloc:
        print("error: invalid URL (missing hostname)")
        sys.exit(1)
main(basepath)