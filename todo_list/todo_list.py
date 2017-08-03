# make a list to handle our schedule
# print out instructions how to use app
# print list
# insert or delete tasks

import os

todo_list=[]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def show_list():
    clear_screen()
    
    print("Todo list :")

    index = 1
    for todo in todo_list:
        print("{}. {}".format(index, todo))
        index += 1

    print("-"*30)

def show_help():
    clear_screen()
    print(54*'*')
    print("Todo_list: let us handle your schedule")
    print("Add new schedule items, print todo list and feel good!")
    print("Simple and practical!")
    print(54*'*')
    print("""
Enter 'DONE' to stop adding tasks.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")
    
  
def add_to_list(todo):
    show_list()
    if len(todo_list):
        position = input("Where should i add '{}'?\n"
                         "Press Enter to add to the end of the list\n"
                         ">>> ".format(todo))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:   
        todo_list.insert(position-1, todo)
    else:   
        todo_list.append(todo)
        
    show_list()

clear_screen()
show_help()

while True:
    new_todo = input("TODO >>> ")

    if new_todo.upper() == 'DONE' or new_todo.upper() == 'QUIT':
        break
    elif new_todo.upper() == "SHOW":
        show_list()
        continue
    elif new_todo.upper() == "HELP":
        show_help()
        continue
    else:
        add_to_list(new_todo)


  


      
    
    