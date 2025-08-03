import os 
filename=input("what is the name of file :")
if os.path.exists(filename):
    print(f"this file {filename} is exist")
else:
    print(f"this file {filename} is not exist")