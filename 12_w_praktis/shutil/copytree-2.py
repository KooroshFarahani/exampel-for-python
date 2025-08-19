import shutil
import os

def copy_tree():
    shutil.copytree("backup","backup2",dirs_exist_ok=True)




copy_tree()