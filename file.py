import os
import re
def modify_filenames(directory_path, file_prefix="", file_suffix="", search_text=None, replace_text=None, simulate=True):
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return
    files_in_directory = os.listdir(directory_path)
    if not files_in_directory:
        print("No files found in the directory.")
        return
    print("\nCurrent Filenames:")
    for file in files_in_directory:
        print(f"- {file}")
    print("\nNew Filenames:")
    for file in files_in_directory:
        full_file_path = os.path.join(directory_path, file)
        if not os.path.isfile(full_file_path):
            continue
        base_name, file_extension = os.path.splitext(file)
        new_filename = base_name
        if search_text and replace_text:
            new_filename = re.sub(search_text, replace_text, new_filename)
        new_filename = f"{file_prefix}{new_filename}{file_suffix}{file_extension}"
        print(f"- {file} -> {new_filename}")
        if not simulate:
            os.rename(full_file_path, os.path.join(directory_path, new_filename))
    if simulate:
        print("\nSimulation mode: No files were renamed.")
    else:
        print("\nFiles renamed successfully.")

if __name__ == "__main__":
    directory_path = input("Enter directory path: ").strip()
    file_prefix = input("Enter prefix (optional): ").strip()
    file_suffix = input("Enter suffix (optional): ").strip()
    search_text = input("Text to replace (optional): ").strip() or None
    replace_text = input("Replace with (optional): ").strip() or None
    simulate = input("Simulate changes? (yes/no): ").strip().lower() == "yes"

    print("\nLoading filenames...")
    modify_filenames(directory_path, file_prefix, file_suffix, search_text, replace_text, simulate)
