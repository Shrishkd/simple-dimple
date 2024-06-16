"""TO DO LIST APPLICATION"""
tasks=[]

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f" '{task}' is sucessfully added in tasks.")
    
def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task {index+1}. {task}")    
    
    
def deleteTask():
    listTask()
    try:
        taskTodelete = int(input("Enter task no. to delete: "))
        if taskTodelete >= 0 and taskTodelete < len(tasks):
            tasks.pop(taskTodelete-1)
            print(f"Task {taskTodelete} has been deleted.")
        else:
            print(f"Task {taskTodelete} was not found.")
    except:
        print("Invalid input.")
        

print ("Welcome to TO DO LIST APP ✨")
while True:
    print ("\n")
    print (" Select one of the following option ⬇️ ")
    print ("--------------------------------------- ")
    print (" 1. Add a new task ➕")
    print ("2. Delete a task 🗑️")
    print ("3. List tasks 📃 ")
    print ("4. Quit ❌ ")
    
    choice = input ("Enter your choice: ")
    
    if(choice=="1"):
        addTask()
    elif(choice=="2"):
        deleteTask()
    elif(choice=="3"):
        listTask()
    elif(choice=="4"):
        break
    else:
        print("ERROR 404: INVALID INPUT")
        
print("See You Again 👋")



