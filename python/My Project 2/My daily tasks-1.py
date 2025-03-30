import os
def clear_screen():
    """Clear the console screen based on the operating system."""
    os.system("cls") if os.name == "nt" else os.system("clear")
tasks=[]
while True:
    print("willcome to the following")
    print("""
          1.add_task
          2.remove_task
          3.view_tasks""")
    user_choice=int(input("please enter your choice:"))
    clear_screen()
    if user_choice==1:    
        tasks.append(input("Please enter your task"))
        print("Task added successfully")
        print(tasks)
        
    elif user_choice==2:
            print(tasks)
            removed_task=input("You can remove a task")
            tasks.remove(removed_task)
            print("Task removed successfully")
            print(tasks)
            
    elif user_choice==3:
        print(tasks)
