# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Messages")
    print("5. <- Go back ")
    print("6. Block users" )
    print("7. View blocked user")
    return input("Please Choose a number: ")

def manageMessagesMenu():
    print("")
    print("1. View messages")
    print("2. Send message")
    print("3. <- Go back")
    return input("Please choose a number: ")