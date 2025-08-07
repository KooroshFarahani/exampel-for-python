
import os
from datetime import datetime
class user():
    def __init__(self,username,email,password,admin=False):
        self.username=username
        self.email=email
        self.password=password
        self.admin=admin
        

    def login(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # get date and time 
        print(f" user name :{self.username} login at {now} welcome ")
        data = f" username : {self.username} \t email : {self.email} \t password : {self.password} \t admin : {self.admin} \t {now} \n"

        with open('log-user.txt','a') as file: # open file to write log login
            file.write(data)
    @staticmethod
    def check_user(user_user):
        
        with open ('log-user.txt','r') as file:
            read=file.read()
            if user_user in read:
                print ("user name is exist")
            else :
                print ("user name in not exist") 
            
    def singin(self):
        pass
    def AdminUser(self):
        pass

    def delete_user(self):
        pass


txt="1.login \n 2.sining \n 3.show user"
print(txt)
user_user = input("enter username :")
#password = input("enter password :")
#email = input("enter the email :")
#admin=bool(input("True or False for admin"))
    
#user1=user(username,email,password,admin)

#user1.login()
user.check_user(user_user)