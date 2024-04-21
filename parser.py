import os

def is_directory_valid(directory):
    """Check if the provided path exists and is a directory."""
    if not os.path.exists(directory):
        print(f"Error: {directory} does not exist.")
        return False
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory.")
        return False
    return True

def contains_uppercase(filename):
    """Check if the filename contains an uppercase letter."""
    return any(char.isupper() for char in filename)

def rename_file_to_lowercase(directory, filename):
    """Rename a single file to lowercase."""
    name, ext = os.path.splitext(filename)
    new_name = name.lower() + ext
    old_file_path = os.path.join(directory, filename)
    new_file_path = os.path.join(directory, new_name)
    
    try:
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_name}")
    except Exception as e:
        print(f"Error renaming {filename}: {e}")

def rename_files_to_lowercase(directory):
    """Rename all files in the directory to lowercase."""
    if not is_directory_valid(directory):
        return

    for filename in os.listdir(directory):
        if contains_uppercase(filename):
            rename_file_to_lowercase(directory, filename)

def get_directory_path_from_user():
    """Prompt the user for the directory path and validate it."""
    while True:
        directory_path = input("Please enter the directory path: ").strip()
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            return directory_path
        print("Error: Please enter a valid directory path.")

def main():
    directory_path = get_directory_path_from_user()
    rename_files_to_lowercase(directory_path)

if __name__ == "__main__":
    main()
