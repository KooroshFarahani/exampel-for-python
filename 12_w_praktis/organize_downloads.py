import os
import shutil

# Define the source folder and destination folders
source_folder = "Downloads"
destination_folders = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"]
}

# Create destination folders if they don't exist
def create_folders():
    for folder in destination_folders:
        folder_path = os.path.join(source_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Move files to corresponding folders based on extension
def organize_files():
    create_folders()
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
            
        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # Check which category the file belongs to
        for folder, extensions in destination_folders.items():
            if ext in extensions:
                dest_path = os.path.join(source_folder, folder, filename)
                try:
                    shutil.move(file_path, dest_path)
                    print(f"Moved {filename} to {folder}")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
                break

if __name__ == "__main__":
    organize_files()