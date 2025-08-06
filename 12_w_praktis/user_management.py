import csv
import os
from datetime import datetime
class user():
    def __init__(self,username,email,password,admin):
        self.username=username
        self.email=email
        self.password=password
        self.admin=admin
    def login(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f" user name :{self.username} login at {now} welcome ")
        data = [['user name ',self.username],['email' , self.email],['password' , self.password],['time login',now],['admin' , self.admin]]
        with open('log-user','a') as file:
            writer =csv.writer(file)
            writer.writerows(data)

            
    def singin(self):
        pass
    def AdminUser(self):
        with open('log-user','r')as file:
            reader=csv.reader(file)
            for row in reader:
                print(row)
                if row == 'True' :
                    print (f"user name : {self.username} is ADMIN")
                else:
                    print (f"user name : {self.username} is NOT ADMIN")

    def delete_user(self):
        pass


txt="1.login \n 2.admin user \n 3.ceart user"
print (txt)
operator=input("please enter the operator : ")
if operator == "1":
    username=input("user name :")
    email=input("enter the email :")
    password=input("enter your password :")
    admin=input("if this user is admin enter true or false :")
    user1=user(username,email,password,admin)
    user1.login()
    print("-----------------------------------")
    user1.AdminUser()
elif operator == "2":
    pass
elif operator=="3":
    pass

    
    
    