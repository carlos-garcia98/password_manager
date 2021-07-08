from user_dao import UserDAO
from werkzeug.security import check_password_hash
from os import system


def welcome():
    welcome = '''
Welcome to your Password Manager!

What would you like to do:
    1) Sign in.
    2) Exit.
Use the appropiate number to choose an action.
> '''

    while True:

        decision = int(input(welcome))
        
        if decision == 1:
            system('cls')
            sign_in()
        elif decision == 2:
            system('cls')
            print('Goodbye!')
            exit()
        else:
            system('cls')
            print('Invalid opcion, please try again.')

def sign_in():
    hashed_password = 'pbkdf2:sha256:260000$58R5RfR8SGZ3dhfm$f30b18300689d90fb2dcdf88232f627102c2ce62bbc2a00003a7eb456624bc71'
    
    sign_in = '''
Welcome to yout Password Manager!

Please enter your password => '''

    while True:

        password = input(sign_in)
        validate_password = check_password_hash(hashed_password, password)
        
        if validate_password:
            system('cls')
            main_menu()
        else:
            system('cls')
            print('Invalid password, try again.')

def main_menu():
    menu = '''
What would you like to do?
    1) List your accounts.
    2) Add an account.
    3) Modify an account.
    4) Delete an account.
    5) Generate a password.
    6) Exit.
Use the appropiate number to choose an action.
 > '''
 
    while True:
        
        decision = int(input(menu))
        
        if decision == 1:
            system('cls')
            # Take to list function.
        elif decision == 2:
            system('cls')
            # Take to add function.
        elif decision == 3:
            system('cls')
            # Take to modify function.
        elif decision == 4:
            system('cls')
            # Take to delete function.
        elif decision == 5:
            system('cls')
            # Take to generate password function.
        elif decision == 6:
            system('cls')
            print('Goodbye!')
            exit()
        else:
            system('cls')
            print('Invalid option, try again.')

def listAccount():
    # list funciton

# Output
welcome()