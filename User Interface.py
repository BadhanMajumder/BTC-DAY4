b = []  
from prettytable import PrettyTable  

def newuser():
    print("Please create an account:")
    user = {}  
    user["UserName"] = input("Enter your name: ")
    user["Email"] = input("Enter your email: ")
    user["Password"] = input("Enter your password: ")
    
    b.append(user)  
    print("User created successfully.")
    
    signin()  

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    for user in b:  
        if user["UserName"] == username and user["Password"] == password:
            print("You have successfully logged in!")
            return
    
    print("Username or password not matched.")
    signin()  

def delete():
    print("Enter the username and password for deletion.")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    for user in b:  
        if user["UserName"] == username and user["Password"] == password:
            b.remove(user)
            print("Account deleted successfully.")
            signin()
            return
    
    print("Username or password not matched.")
    signin()  

def table():
    if not b:
        print("No users available to display.")
        signin()
        return

    table = PrettyTable()       
    table.field_names = ["UserName", "Email", "Password"]

    for user in b:
        table.add_row([user["UserName"], user["Email"], user["Password"]])

    print(table)
    signin()  

def signin():
    try:
        a = int(input("Enter 1 to create a new user, 2 to log in, 3 to delete an account, or 4 to view all users: "))
        if a == 1:
            newuser()
        elif a == 2:
            login()
        elif a == 3:
            delete()
        elif a == 4:
            table()
        else:
            print("Invalid choice. Try again.")
            signin()
    except ValueError:
        print("Please enter a valid number.")
        signin()
signin()
