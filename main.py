import os
import shutil
from gencontent import generate_page

from textnode import TextNode, TextType
from copystatic import copy_source_to_destination

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    node = TextNode("bunny", TextType.bold, "bunny.com")
    print(node)

    if os.path.exists(dir_path_public):
        # delete all the contents of the destination directory (public) to ensure that the copy is clean
        shutil.rmtree(dir_path_public)
    copy_source_to_destination(dir_path_static, dir_path_public)

generate_pages_recursive("content", "template.html", "public")

main()










