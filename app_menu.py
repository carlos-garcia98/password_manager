from user_dao import UserDAO
from users import User
from logger_base import log
from werkzeug.security import check_password_hash
from os import system
import pyperclip as pc
import stdiomask
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
    # You can change the content of this variable with another hashed password, so you can use your own master password.
    hashed_password = 'pbkdf2:sha256:260000$58R5RfR8SGZ3dhfm$f30b18300689d90fb2dcdf88232f627102c2ce62bbc2a00003a7eb456624bc71' 
    
    sign_in = '''
Welcome to yout Password Manager!

Please enter your password => '''

    while True:

        # password = input(sign_in)
        password = stdiomask.getpass(prompt=sign_in)
        validate_password = check_password_hash(hashed_password, password)
        
        if validate_password:
            system('cls')
            mainMenu()
        else:
            system('cls')
            print('Invalid password, try again.')

def mainMenu():
    menu = '''
What would you like to do?
    1) List your accounts.
    2) Search an account.
    3) Get the password of an account.
    4) Add an account.
    5) Modify an account.
    6) Delete an account.
    7) Generate a password.
    8) Exit.
Use the appropiate number to choose an action.
 > '''
 
    while True:
        
        decision = int(input(menu))
        
        if decision == 1:
            system('cls')
            listAccount()
        elif decision == 2:
            system('cls')
            SearchAccountMenu()
        elif decision == 3:
            system('cls')
            getPasswordMenu()
        elif decision == 4:
            system('cls')
            addAccount()
        elif decision == 5:
            system('cls')
            modifyAccount()
        elif decision == 6:
            system('cls')
            deleteAccount()
        elif decision == 7:
            system('cls')
            generatePassword()
        elif decision == 8:
            system('cls')
            print('Goodbye!')
            exit()
        else:
            system('cls')
            print('Invalid option, try again.')

def SearchAccountMenu():
    menu = '''
How would you like to search your account?
    1) Search by ID.
    2) Search by App Name.
    3) Return to main menu.
Use the appropiate number to choose an action.
 > '''
 
    while True:
        
        decision = int(input(menu))
        
        if decision == 1:
            system('cls')
            searchByID()
        elif decision == 2:
            system('cls')
            searchByAppName()
        elif decision == 3:
            system('cls')
            mainMenu()
        else:
            system('cls')
            print('Invalid option, try again.')

def getPasswordMenu():
    menu = '''
How would you like to select the account?
    1) By ID.
    2) By App Name.
    3) Return to main menu.
Use the appropiate number to choose an action.
 > '''
 
    while True:
        
        decision = int(input(menu))
        
        if decision == 1:
            system('cls')
            getPasswordByID()
        elif decision == 2:
            system('cls')
            getPasswordByAppName()
        elif decision == 3:
            system('cls')
            mainMenu()
        else:
            system('cls')
            print('Invalid option, try again.')

def searchByID():
    idAccount = input('Enter the ID to search => ')
    
    accounts = User(id_account=idAccount)
    results = UserDAO.searchById(accounts)
    print('\n')
    print('Results:')
    if results == []:
        log.info('There is not an account with the ID provided.')
    else:
        for i in results:
            log.info(i)

def searchByAppName():
    appName = input('Enter the app name to search => ')
    
    accounts = User(app_name=appName)
    results = UserDAO.searchByAppName(accounts)
    print('\n')
    print('Results:')
    if results == []:
        log.info('There are no accounts with the app name you provided => ')
    else:
        for i in results:
            log.info(i)

def listAccount():
    accounts = UserDAO.select()
    if accounts == []:
        log.info('You have no accounts stored.')
    else:
        for i in accounts:
            log.info(i)

def addAccount():
    app_name = input('Enter de site or app name => ')
    username = input('Enter the username => ')
    password = input('Enter the password => ')
    url = input('Enter the url => ')
    print('\n')
    account = User(app_name=app_name, username=username, password=password, url=url) 
    inserted_account = UserDAO.insert(account)
    print('\n')
    log.info(f'Inserted accounts: {inserted_account}')
    
def modifyAccount():
    app_name = input('Enter the site or app name => ')
    username = input('Enter the username => ')
    password = input('Enter the password => ')
    url = input('Enter the url => ')
    id_account = int(input('Enter the id_account => '))
    print('\n')
    account = User(app_name=app_name, username=username, password=password, url=url, id_account=id_account)
    modified_accounts = UserDAO.update(account)
    print('\n')
    log.info(f'Modified accounts: {modified_accounts}')
    
def deleteAccount():
    id_account = int(input('Enter the account id you would like to delete => '))
    print('\n')
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

def getPasswordByID():
    idAccount = input('Enter the ID => ')
    
    password = User(id_account=idAccount)
    result = UserDAO.getPasswordID(password)
    print('\n')
    print('Result:')
    if result == []:
        log.info('The ID provided couldn\'t be found.')
    else:
        for i in result:
            pc.copy(i)
            log.info(i)
        print('\n')
        print('The password has been copied to your clipboard.')

def getPasswordByAppName():
    appName = input('Enter the app name => ')
    
    password = User(app_name=appName)
    result = UserDAO.getPasswordAppName(password)
    print('\n')
    print('Result:')
    if result == []:
        log.info('The ID provided couldn\'t be found.')
    else:
        for i in result:
            pc.copy(i)
            log.info(i)
        print('\n')
        print('The password has been copied to your clipboard.')

# Output
welcome()