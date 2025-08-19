import os
import shutil

src=os.path.join("C:/Users/k.farahani/Desktop/github/exampel-for-python","12_w_praktis","shutil")
dst=os.path.join("exampel-for-python","12_w_praktis","shutil")

def mak_folder():
    try:
        os.makedirs(os.path.join(src,"project","logs"), exist_ok=True)
        with open(os.path.join(src,"project","main.py"), "w") as f:
            f.write("print('Hello')")
        with open(os.path.join(src,"project","logs","log1.txt"), "w") as f:
            f.write("Log 1")
        with open(os.path.join(src,"project","logs","log2.txt"), "w") as f:
            f.write("Log 2")
    except:
        print("file project , log sakhte nashod")
mak_folder()