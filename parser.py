import os

def rename_files_to_convention(directory):
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Check if the file name starts with an uppercase letter
        if filename[0].isupper():
            # Construct the new file name with the first character in lowercase
            new_filename = filename[0].lower() + filename[1:]
            
            # Get the full paths of the old and new files
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")
        
        # Check if the file name doesn't follow the convention example-example
        elif not filename.replace('-', '').isalnum() or '-' not in filename:
            # Construct the new file name with the naming convention example-example
            words = filename.split('-')
            new_filename = '-'.join([word.lower() for word in words])
            
            # Get the full paths of the old and new files
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")

# Specify the directory you want to process
directory_path = '/path/to/your/directory'

# Call the function to rename files
rename_files_to_convention(directory_path)
