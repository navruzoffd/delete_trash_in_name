import os

def rename_files_and_directories(start_dir, text_to_remove):
    count_files, count_dir = 0, 0
    for root, dirs, files in os.walk(start_dir, topdown=False):
        
        for name in files:
            if text_to_remove in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(text_to_remove, '')
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                count_files += 1

        for name in dirs:
            if text_to_remove in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(text_to_remove, '')
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                count_dir += 1

    print(f"Renamed {count_files} files and {count_dir} directories")

# Set text to remove
text_to_remove = ""

# Set start directory
start_directory = ""

rename_files_and_directories(start_directory, text_to_remove)