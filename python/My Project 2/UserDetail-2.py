import time
import os

def clear_screen():     
    os.system("cls") if os.name == "nt" else os.system("clear")

class UserDetail:
    def __init__(self, name, last_name, email, password, status="inactive"):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display(self):
        return (f"First name: {self.name}\n"
                f"Last name: {self.last_name}\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}\n"
                f"Status: {self.status}\n"
                "____________________\n")
        
def create_user():
   name = input("Enter first name: ")
   last_name = input("Enter last name: ")
   email = input("Enter email: ")
   password = input("Enter password: ")
   return UserDetail(name, last_name, email, password)

   
users = []

while True:
    print("""Welcome to user management
          
          Choose an Action:
          1. Add new user
          2. Display all users
          3. Exit
           """)
    user_choice = input("Enter your choice: ")
    
    if user_choice == "1":
        users.append(create_user())
        print("User added successfully!")
        time.sleep()
        
    elif user_choice == "2":
        clear_screen()
        print("Display all users....")        
        print()
        time.sleep(1)
        
        if users:
          for I in users:
             print(I.display())
          time.sleep(1)   
        else:
            print("sorry, didn't find any user to display!")
            time.sleep(2)
        
    elif user_choice == "3":
        print("Exiting")
        time.sleep(2)
        break

    else:
        print("Enter just 1,2,or 3.")
        clear_screen()