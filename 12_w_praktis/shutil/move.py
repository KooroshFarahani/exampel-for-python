import os
import shutil

def Make_folder():
    try:
        if not os.path.exists("archive"):
            os.mkdir("archive")
        else:
            raise ValueError("file exist")
    except ValueError as e:
        print (f"error {e}")
def Move():
    try:
        if not os.path.exists("log.txt"):
            raise ValueError("file is not exist :")
        else:
            shutil.move("log.txt","archive/log.txt")
    except ValueError as e:
        print (f"Error {e}")

Make_folder()
Move()
