from database import Connection
from users import User
from logger_base import log
from os import system
import pyperclip as pc
import stdiomask
import random
import hashlib

# Functions
def welcome():
    welcome = '''
Welcome to your Password Manager!

What would you like to do:
    1) Sign in.
    2) Exit.
Use the appropiate number to choose an action.
> '''

    Connection.create_table()
    Connection.create_mp_table()

    while True:
        try:
            
                decision = int(input(welcome))
                
                if decision == 1:
                    system('cls')
                    check = Connection.select_mp()
                    if check:
                        sign_in()
                    else:
                        setMasterPassword()
                elif decision == 2:
                    system('cls')
                    Connection.get_connection().close()
                    print('Goodbye!')
                    exit()
                else:
                    system('cls')
                    print('Invalid opcion, please try again.')
        except ValueError:
            system('cls')
            print('Invalid value, please try again.')    
    

def setMasterPassword():
    while True:
        
        print('Please set your master password:')
        password1 = stdiomask.getpass(prompt='Enter the password => ')
        password2 = stdiomask.getpass(prompt='Re-enter the password => ')
        
        if password1 == password2:
            hash_password = hashlib.md5(password1.encode('utf-8'))
            encrypt_password = hash_password.hexdigest()
            Connection.insert_mp(encrypt_password)
            system('cls')
            sign_in()
        else:
            system('cls')
            print('Passwords does not match.')

def sign_in():
    sign_in = '''
Welcome to yout Password Manager!

Please enter your password => '''

    while True:

        password = stdiomask.getpass(prompt=sign_in)
        hashed_password = hashlib.md5(password.encode('utf-8'))
        encrypt_password = hashed_password.hexdigest()
        validate_password = Connection.select_password_mp(encrypt_password)
        
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
        try:
            
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
                Connection.get_connection().close()
                print('Goodbye!')
                exit()
            else:
                system('cls')
                print('Invalid option, try again.')
        except ValueError:
            system('cls')
            print('Invalid value, try again.')

def SearchAccountMenu():
    menu = '''
How would you like to search your account?
    1) Search by ID.
    2) Search by App Name.
    3) Return to main menu.
Use the appropiate number to choose an action.
 > '''
 
    while True:
        try:
            
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
        except ValueError:
            system('cls')
            print('Invalid value, try again.')

def getPasswordMenu():
    menu = '''
How would you like to select the account?
    1) By ID.
    2) By App Name.
    3) Return to main menu.
Use the appropiate number to choose an action.
 > '''
 
    while True:
        try:
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
        except ValueError:
            system('cls')
            print('Invalid value, try again.')

def searchByID():
    idAccount = input('Enter the ID to search => ')
    
    accounts = User(id_account=idAccount)
    results = Connection.select_by_id(accounts)
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
    results = Connection.select_by_app_name(accounts)
    print('\n')
    print('Results:')
    if results == []:
        log.info('There are no accounts with the app name you provided.')
    else:
        for i in results:
            log.info(i)

def listAccount():
    accounts = Connection.select()
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
    inserted_account = Connection.insert(account)
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
    modified_accounts = Connection.update(account)
    print('\n')
    log.info(f'Modified accounts: {modified_accounts}')
    
def deleteAccount():
    id_account = int(input('Enter the account id you would like to delete => '))
    print('\n')
    account = User(id_account=id_account)
    deleted_account = Connection.delete(account)
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
    result = Connection.get_password_by_id(password)
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
    result = Connection.get_password_by_app_name(password)
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