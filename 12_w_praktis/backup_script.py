import os
import shutil
import argparse
from datetime import datetime

# Set up argument parser
parser = argparse.ArgumentParser(description="Backup files from source to destination folder.")
parser.add_argument("source", help="Path to the source folder")
parser.add_argument("--dest", help="Path to the destination backup folder (default: backup_YYYY-MM-DD)", default=None)
args = parser.parse_args()

# Define source and destination folders
source_folder = args.source
backup_folder = args.dest if args.dest else f"backup_{datetime.now().strftime('%Y-%m-%d')}"

# Create backup folder if it doesn't exist
def create_backup_folder():
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

# Copy all contents from source to backup folder
def backup_files():
    # Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return
    
    create_backup_folder()
    
    for item in os.listdir(source_folder):
        source_path = os.path.join(source_folder, item)
        dest_path = os.path.join(backup_folder, item)
        
        try:
            # Copy files and directories recursively
            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy2(source_path, dest_path)
            print(f"Copied {item} to {backup_folder}")
        except Exception as e:
            print(f"Error copying {item}: {e}")

if __name__ == "__main__":
    backup_files()