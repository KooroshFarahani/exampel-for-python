import os
import shutil

def make_folder():
    src = r"C:/Users/k.farahani/Desktop/github/exampel-for-python/12_w_praktis/shutil/archive"
    dst = r"C:/Users/k.farahani/Desktop/github/exampel-for-python/12_w_praktis/shutil/temp_folder"

    # Check if source folder exists
    if not os.path.exists(src):
        print(f"❌ Source folder not found: {src}")
        # Create a test file in temp_folder for testing
        os.makedirs(dst, exist_ok=True)
        test_file = os.path.join(dst, "test_file.txt")
        with open(test_file, "wb") as f:
            f.write(b"X" * 1024 * 1024)  # Create a 1MB test file
        print(f"🗃️ Created test file in {dst} for testing")
        return

    # If destination folder exists, delete it first
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"🗑️ Old folder deleted: {dst}")

    # copytree creates the destination folder, no need for mkdir
    try:
        shutil.copytree(src, dst)
        print(f"✅ Copy successful: {src} → {dst}")
    except Exception as e:
        print(f"❌ Copy error: {e}")

def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size  # Return size in bytes

def disk_usage():
    folder = r"C:/Users/k.farahani/Desktop/github/exampel-for-python/12_w_praktis/shutil/temp_folder"  # Correct path

    if not os.path.exists(folder):
        print(f"❌ Folder does not exist: {folder}")
        return

    # Calculate size of temp_folder
    folder_size = get_folder_size(folder)
    print(f"📏 Size of temp_folder: {folder_size} bytes")

    # Before deletion
    total, used, free = shutil.disk_usage(folder)
    print("=== Before deletion ===")
    print(f"Total space: {total} bytes")
    print(f"Used space: {used} bytes")
    print(f"Free space: {free} bytes")

    # Delete the entire temp_folder
    try:
        shutil.rmtree(folder)
        print(f"🗑️ temp_folder deleted: {folder}")
    except Exception as e:
        print(f"❌ Error deleting temp_folder: {e}")

    # After deletion
    parent_folder = os.path.dirname(folder)  # Get parent directory to check disk usage
    total_new, used_new, free_new = shutil.disk_usage(parent_folder)
    print("=== After deletion ===")
    print(f"Total space: {total_new} bytes")
    print(f"Used space: {used_new} bytes")
    print(f"Free space: {free_new} bytes")

# Run
make_folder()
disk_usage()