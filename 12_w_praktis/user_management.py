
import os
from datetime import datetime
class user():
    def __init__(self,username,email,password,admin=False):
       
        self.username=username
        self.email=email
        self.password=password
        self.admin=admin
        

    def singin(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # get date and time 
        print(f" user name :{self.username} singin at {now} welcome ")
        data = f" username : {self.username} \t email : {self.email} \t password : {self.password} \t admin : {self.admin} \t {now} \n"

        with open('log-user.txt','a') as file: # open file to write log login
            file.write(data)
    @staticmethod
    def login (user_user,pass_pass):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open ('log-user.txt','r') as file:
            read=file.read()
            if user_user in read and pass_pass in read :
                print(f" user name :{user_user} login at {now} welcome ")
                return True
            else:
                print ("user name in not exist") 
                return False
    def AdminUser(self):
        pass

    def delete_user(self):
        pass


txt="1.singin \n 2.login \n 3.show user"
print(txt)

operator=input("enter the chose :")

if operator=="1":
    username=input("Please Enter the Username :")
    email=input("Please Enter the Email :")
    password=input("Please Enter the Password :")
    admin=bool(input("Please Enter the Admin (True or False) :"))
    user_create = user(username,email,password,admin)
    user_create.singin()

elif operator=="2":
    username=input("Please Enter the Username :")
    password=input("Please Enter the Password :")
    if user.login(username,password):
        print("\t")
    else:
        user.login(username,password)
else:
    pass
