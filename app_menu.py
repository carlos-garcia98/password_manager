from user_dao import UserDAO
from users import User
from logger_base import log
from werkzeug.security import check_password_hash
from os import system
import pyperclip as pc
import random

# Functions
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
    hashed_password = 'pbkdf2:sha256:260000$58R5RfR8SGZ3dhfm$f30b18300689d90fb2dcdf88232f627102c2ce62bbc2a00003a7eb456624bc71' # You can change the content of this variable with another hashed password, so you can use your own master password.
    
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
            # system('cls')
            listAccount()
            # break
        elif decision == 2:
            # system('cls')
            addAccount()
        elif decision == 3:
            # system('cls')
            modifyAccount()
        elif decision == 4:
            # system('cls')
            deleteAccount()
        elif decision == 5:
            # system('cls')
            generatePassword()
        elif decision == 6:
            # system('cls')
            print('Goodbye!')
            exit()
        else:
            system('cls')
            print('Invalid option, try again.')

def listAccount():
    accounts = UserDAO.select()
    print('\n')
    for i in accounts:
        log.info(i)

def addAccount():
    print('\n')
    app_name = input('Enter de site or app name => ')
    username = input('Enter the username => ')
    password = input('Enter the password => ')
    url = input('Enter the url => ')
    print('\n')
    
    account = User(app_name=app_name, username=username, password=password, url=url) 
    inserted_account = UserDAO.insert(account)
    log.info(f'Inserted accounts: {inserted_account}')
    
def modifyAccount():
    app_name = input('Enter the site or app name => ')
    username = input('Enter the username => ')
    password = input('Enter the password => ')
    url = input('Enter the url => ')
    id_account = int(input('Enter the id_account => '))
    
    account = User(app_name=app_name, username=username, password=password, url=url, id_account=id_account)
    modified_accounts = UserDAO.update(account)
    print('\n')
    log.info(f'Modified accounts: {modified_accounts}')
    
def deleteAccount():
    id_account = int(input('Enter the account id you would like to delete => '))
    
    account = User(id_account=id_account)
    deleted_account = UserDAO.delete(account)
    print('\n')
    log.info(f'Deleted accounts: {deleted_account}')

def generatePassword():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    char_mayus = characters.upper()
    symbols = '~`!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'
    all_chars = characters + char_mayus + symbols
    
    length = int(input('Enter the length of your password => '))
    
    for i in range(1):
        a = random.sample(all_chars, length)
        password = ''.join(a)
        pc.copy(password)
        print('\n')
        print(f'Here is your password: {password}')
        print('Your password has been copied to the clipboard.')

# Output
welcome()