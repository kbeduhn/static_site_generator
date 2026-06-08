from block_to_html import markdown_to_html_node
import os
from pathlib import PurePath

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    # Print a message like "Generating page from from_path to dest_path using template_path".
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path) as f:
        from_contents = f.read()

    # Read the template file at template_path and store the contents in a variable.
    with open(template_path) as f:
        template_contents = f.read()

    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    node = markdown_to_html_node(from_contents)
    html_string = node.to_html()

    # Use the extract_title function to grab the title of the page.
    page_title = extract_title(from_contents)

    # Replace {{ Title }} and {{ Content }} in the template
    # Write the final HTML to dest_path (creating directories if needed)
    #The string .replace() method and os.makedirs + os.path.dirname will be your friends here.

    final_html = template_contents.replace("{{ Title }}", page_title)
    final_html = final_html.replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        # If it's a directory, call generate_pages_recursive() but pass the matching subdirectory inside the destination too
        if not os.path.isfile(from_path):
            generate_pages_recursive(from_path, template_path, dest_path)
        # If it's a file, only handle .md files, compute the output path by changing index.md to index.html, call your existing single-page generator
        else:
            if from_path.endswith('.md'):
                # compute the output path by changing index.md to index.html
                p = PurePath(dest_path)
                dest_path = p.with_suffix('.html')
                # call your existing single-page generator
                generate_page(from_path, template_path, dest_path)


















