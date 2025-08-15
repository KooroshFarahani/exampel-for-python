import os
from datetime import datetime

def folder_viewer():
    try:
        p=input("Enter the path (input dubel \) :")
        for item in os.listdir(p):
            time = os.path.getctime(item)
            print(item , datetime.fromtimestamp(time))
    except:
        print (f"your path is not corect {p}")
print ("---------------------------------------")
folder_viewer()

print ("---------------------------------------")
