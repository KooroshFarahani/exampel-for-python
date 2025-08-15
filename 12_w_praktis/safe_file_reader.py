try:
    file_name = input("enter the file name :")
    with open (file_name , 'r') as file :
        f=file.read()
        print(f)
       
except FileNotFoundError:
   print("File not found!")
finally:
    print("your file is close")