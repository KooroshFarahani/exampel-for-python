import os 
import shutil

def creatfile ():
    if not os.path.exists("backup"):
        os.mkdir("backup")
    else:
        with open("test.txt",'w')as file:
            file.write("lajdfkvbjsdkvjbskdjbvksjbdvikjb")
def copy():
    shutil.copy2("test.txt","backup/test.txt")
    shutil.copy("test.txt","backup/test2.txt")
creatfile()
copy()
