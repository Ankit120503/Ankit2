# empty dictionary 
phoneDirectory = {}

# Define the menu function
def menu():
    print("\nWELCOME TO THE GRANN'S PHONE DIRECTORY ")
    print("\nMenu\n")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

#  addRecord function
def addRecord():
    name = input("\nEnter name: ")
    phoneNumber = input("Enter your 10-digit phone number: ")
    phoneDirectory[name] = phoneNumber
    print("Record added")

#  searchRecord function
def searchRecord():
    name = input("\nEnter name to search: ")
    if name in phoneDirectory:
        print(name + ": " + phoneDirectory[name])
    else:
        print(name + " not found")

#  changeRecord function
def changeRecord():
    name = input("\nEnter name: ")
    if name in phoneDirectory:
        phoneNumber = input("Enter new 10-digit phone number: ")
        phoneDirectory[name] = phoneNumber
        print("Record updated")
    else:
        print(name + " not found")

#  delete Record function
def deleteRecord():
    name = input("\nEnter name: ")
    if name in phoneDirectory:
        del phoneDirectory[name]
        print("Record deleted")
    else:
        print(name + " not found")

#  menu
menu()
choice = int(input("\nEnter your choice: "))

# Loop 
while choice != 5:
    if choice == 1:
        addRecord()
    elif choice == 2:
        searchRecord()
    elif choice == 3:
        changeRecord()
    elif choice == 4:
        deleteRecord()
    else:
         print("Invalid choice ")
    
    #  user input again
    menu()
    choice = int(input("\nEnter your choice: "))
    
print("\nExiting phone directory")
