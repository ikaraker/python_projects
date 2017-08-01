#make a list to hold onto our items
#print out instructions how to use app

def print_list(my_list):
    print("Todo list : {}".format(", ".join(my_list)))

def help_me():
    print("Todo_list: let us handle your schedule")
    print("Add new schedule items, print todo list and feel good!")
    print("Simple and practical!")
  
def add_to_list(my_list, todo_item):
    my_list.append(todo_item)
    print("Item {} added, list has {} items".format(todo_item, len(my_list)))


def my_todo_list():
    todo=""
    todo_list=[]
    print("What should we do today?")
    print("Enter DONE to terminate...")
    
    while(todo != "DONE"):
        todo = input("Give a TODO >>> ")
        if todo == "SHOW":
            print_list(todo_list)
            continue
        elif todo == "HELP":
            help_me()
            continue
        else:
            if not todo == "DONE":
                add_to_list(todo_list, todo)
    return todo_list
  

  
mylist = my_todo_list()
print_list(mylist) 
    
        
      
    
    