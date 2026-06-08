import os
import shutil
import sys
from gencontent import generate_page, generate_pages_recursive

from textnode import TextNode, TextType
from copystatic import copy_source_to_destination

dir_path_static = "./static"
dir_path_public = "./docs"

def main():
    if os.path.exists(dir_path_public):
        # delete all the contents of the destination directory (public) to ensure that the copy is clean
        shutil.rmtree(dir_path_public)
    copy_source_to_destination(dir_path_static, dir_path_public)

    # use the sys.argv to grab the first CLI argument to the program. Save it as the basepath. If one isn't provided, default to /.
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    # Pass the basepath to the generate_pages_recursive and generate_page functions.
    generate_pages_recursive("content", "template.html", dir_path_public, basepath)

main()

