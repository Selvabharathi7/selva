from Products import item
import re

username="selva"
password="Selva@12"
class validate:
    def pass_valid(self,word):
            if (re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",word)):
                return word
            else:
                print("Does not contain word or number or less than 6 letters \n Enter password again")
                word=input()
            
class login():
    def __init__(self,username,password):
            print("1.Login\n2.Register")
            temp=int(input("Enter 1 to  login or 2 to register: "))
            if temp == 1:
                login.authentication(self,username,password)
            if temp == 2:
                username=input("Uname: ")
                p=input("Password: ")
                password=validate.pass_valid(self,p)
                print("Registerd Successfull!!!\nLogin Please")
                login.authentication(self,username,password)
        
    def authentication(self,username,password):
        user=input("name: ") 
        pswd=input("password: ")
        check=validate.pass_valid(self,pswd)
        if user==username and check==password:
            print("Login Success!\n\t\t\tWelcome to Zomato\t\t\t")
            print("Breakfast -> 1\nDinner -> 2")
            number = int(input())
            if(number == 1):
               item.breakfast(self)
            else:
               item.dinner(self)
        else:
            print(password)
            print("Enter Your Valid input:")
            login.authentication(self,username,password)   

# login(username,password)
item()


