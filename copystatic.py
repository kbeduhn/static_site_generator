import os
import shutil

def copy_source_to_destination(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        # recreate the empty public dir with os.mkdir
        os.mkdir(dest_dir_path)

    # copy all files and subdirectories, nested files, etc
    for item in os.listdir(source_dir_path):
        item_path = os.path.join(source_dir_path, item)
        dest_path = os.path.join(dest_dir_path, item)
        old_path = source_dir_path
        new_path = dest_dir_path
        if os.path.isfile(item_path):
            shutil.copyfile(item_path, dest_path)
            print(f"old path: {old_path} -> new path: {new_path}")
        else:
            copy_source_to_destination(item_path, dest_path)
