import time 
import os 

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class GymMembership():
    def __init__(self, first_name, last_name, membership_ID, status):
        self.first_name = first_name
        self.last_name = last_name  
        self.membership_ID = membership_ID  
        self.status = status 
    
    def display(self):
        return (f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Membership ID: {self.membership_ID}\n"
                f"Membership Status: {self.status}\n"
                f"_____________________\n")   

def create_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    membership_ID = input("Enter membership ID: ")
    status = input("Enter membership status, or press enter to leave as inactive: ")
    print("Member added successfully!")
    
    if not status:
        status = "inactive"   
    return GymMembership(first_name, last_name, membership_ID, status) 

def search_user(list_membership):
    clear_screen()
    print(f"Search by:\n\n"
          f"1. Membership ID\n"
          f"2. First Name\n"
          f"3. Membership Status\n")    
    search_choice = input("Enter your choice: ")
    
    found_members = []
    
    if search_choice == "1":
        search_ID = input("Enter the membership ID to search: ")
        for D in list_membership:
            if search_ID == D.membership_ID:
                found_members.append(D)
                
    elif search_choice == "2":
        search_firstname = input("Enter the first name to search: ")
        for f in list_membership:
            if search_firstname.lower() == f.first_name.lower():
                found_members.append(f)
                
    elif search_choice == "3":
        search_status = input("Enter the membership status to search (active/inactive): ")
        for s in list_membership:
            if search_status.lower() == s.status.lower():
                found_members.append(s)
    
    if found_members:
        print("Found memberships:")
        for users in found_members:
            print(users.display())
            time.sleep(2)
    else:
        print("No memberships found with the given criteria.")
        time.sleep(2)

list_membership = []     

while True:
    clear_screen()
    print(f"Welcome to Gym Membership Management\n\n"
          f"Choose an Action:\n\n"
          f"1. Add new member\n"
          f"2. Display all members\n"
          f"3. Search for a member\n"
          f"4. Exit\n") 
    
    user_choice = input("Enter your choice: ")
    if user_choice == "1": 
        clear_screen()
        list_membership.append(create_user())
        time.sleep(3)
        
    elif user_choice == "2":
        clear_screen()
        if list_membership:
            print("Displaying all members.....")
            for I in list_membership:
                print(I.display())
        else:
            print("There are no memberships.")
        time.sleep(3)
        
    elif user_choice == "3":
        if list_membership:
            search_user(list_membership)
        else:
            print("No members to search.")
            time.sleep(2)  
    
    elif user_choice == "4":
        print("Exiting......")
        time.sleep(3)  
        break 
    
    else:
        print("Please enter just 1, 2, 3, or 4.")
        time.sleep(2) 
        clear_screen()
