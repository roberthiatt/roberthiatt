#----------------------------------------------------------------------------------------------------#
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each row of data
#              in "ToDoList.txt" into a Python Dictionary.
#              Add each dictionary row to a Python list table
# ChangeLog (Who,When,What):
#                           RRoot,1.1.2030,Created starter script
#                           RHiatt,2.16.2021,Added code to complete Assignment05
#----------------------------------------------------------------------------------------------------#
objFile = open("C:\Python\_PythonClass\Assignment05\ToDoList.txt", "a")

# -- Data -- #              # declare variables and constants

objFile = "C:\Python\_PythonClass\Assignment05\ToDoList.txt"    # An object that represents a file
strData = ""                # A row of text data from the file
dicRow = {}                 # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []               # A list that acts as a "table" of rows
strChoice = ""              # A capture-the-user option selection
strMenu = ""

# -- Processing -- #
# Step 1: When the program starts, load any data you have
# in a text file called ToDoList.txt into a Python list of dictionary rows (like Lab 5-2)

file = open(objFile,"r")
for i in file:
    lstRow = i.split(",") # Split the rows, turn into list
    dicRow = {"Task":lstRow[0].strip(), "Priority":lstRow[1].strip()} # take the list and put index 0 and 1 in dictionary
    lstTable.append(dicRow)
file.close()

# -- Input/Output -- #
# Step 2: Display a menu of choices to the user
while(True):
    print("""
    Menu of Options:
    
    1) Show Current Data
    2) Add a New Item
    3) Remove an Existing Item
    4) Save Data to File
    5) Exit Program   
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] -> "))
    print() # Adding a new line for aesthetics

    # Step 3: Show the current items in the table
    if(strChoice.strip() == '1'):
        print("Please see below for the current data: ")
        print()  # Adding a new line for aesthetics
        for i in lstTable:
            print(i["Task"] + ", " + i["Priority"])
        continue
    # Step 4: Add a new item to the List/Table
    elif(strChoice.strip() == '2'):
        taskName = input("Please type in the new task's name: ")
        taskPriority = input("Please type in the new task's priority: ")
        dicRow = {"Task":taskName, "Priority":taskPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove an item from the List/Table based on its name
    elif(strChoice.strip() == '3'):
        print("Here is the current list: ")
        print() # Adding a new line for aesthetics
        for i in lstTable:
            print(i["Task"] + ", " + i["Priority"])
        print() # Adding a new line for aesthetics
        taskRemove = input("Please type in the name of the task you'd like to remove: ")
        for i in lstTable:
            if i["Task"] == taskRemove:
                lstTable.remove(i)
            else:
                print("The task you entered is not in the list.")
        print()  # Adding a new line for aesthetics
        print("Here is the current list: ")
        print() # Adding a new line for aesthetics
        for i in lstTable:
            print(i["Task"] + ", " + i["Priority"])
        continue
    # Step 6: Save tasks to the ToDoList.txt file
    elif(strChoice.strip() == '4'):
        objFile = open(objFile, "a")
        for i in lstTable:
            objFile.write(i["Task"] + "," + i["Priority"] + "\n")
        file.close()
        print("Data Saved!")
        continue
    # Step 7 - Exit program
    elif(strChoice.strip() == '5'):
        print("Thank you for your time. See you soon!")
        break # and Exit program