import os
import shutil

def make_folder():
    try:
        if not os.path.exists("archive"):
            os.mkdir("archive")
        else:
            raise ValueError("!!folder is exist !!")
    except ValueError as e:
        print (f"Error {e}")
def make_archive():
    try:
        if not os.path.exists("archive_zip"):
            shutil.make_archive("archive_zip","zip","archive")
        else:
            raise ValueError("the file is ziped")
    except ValueError as e:
        print (f"Error{e}")

def unarchive():
    try:
        if not os.path.exists("archive_zip.zip"):
            raise ValueError("!!! the file not found !!!")
        else:
            shutil.unpack_archive("archive_zip.zip","new_unarchive","zip")
    except ValueError as e:
        print(f"Error{e}")

make_folder()
make_archive()
unarchive()