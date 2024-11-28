import os
import shutil

def rename_files_sequentially(folder_path, prefix='file_'):
    """
    Rename all files in a folder sequentially while preserving their extensions.
    
    Args:
        folder_path (str): Path to the folder containing files
        prefix (str): Prefix to use for the new filenames (default: 'file_')
    """
    # Define the test data directory path
    test_data_folder = os.path.join(folder_path, "../scream test data")
    os.makedirs(test_data_folder, exist_ok=True)

    # List of specific files to copy to the test data folder
    test_files = [
        "1289.wav", "1290.wav", "1291.wav", "1292.wav", 
        "1293.wav", "1294.wav", "1295.wav", "1296.wav"
    ]
    
    # Get list of files in the folder
    files = os.listdir(folder_path)
    
    # Filter out directories, only keep files
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    # Sort files to ensure consistent ordering
    files.sort()
    
    # Counter for sequential numbering
    counter = 1
    
    # Store original and new names to avoid conflicts
    rename_mapping = {}
    
    # Create mapping of original to new names
    for filename in files:
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Create new filename with padding zeros (001, 002, etc.)
        new_name = f"{prefix}{str(counter).zfill(3)}{file_extension}"
        
        # Store the mapping
        rename_mapping[filename] = new_name
        counter += 1
    
    # Perform the actual renaming and check for test files
    for old_name, new_name in rename_mapping.items():
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} → {new_name}")
        
        # If the file is in the test_files list, copy it to the test data folder
        if old_name in test_files:
            test_data_path = os.path.join(test_data_folder, new_name)
            shutil.copy(new_path, test_data_path)
            print(f"Copied {new_name} to test data folder")


def rename_files(folder_path, prefix):
    files = os.listdir(folder_path)
    total_files = len(files)
    padding = len(str(total_files))
    
    for index, filename in enumerate(sorted(files), 1):
        old_path = os.path.join(folder_path, filename)
        new_name = f"{prefix}{str(index).zfill(4)}{os.path.splitext(filename)[1]}"
        new_path = os.path.join(folder_path, new_name)
        print(f"Renamed: {old_path} → {new_name}")
        os.rename(old_path, new_path)



# Example usage
if __name__ == "__main__":
    folder_path = "DataSet/scream"
    prefix = "s_"
    rename_files(folder_path,prefix)
