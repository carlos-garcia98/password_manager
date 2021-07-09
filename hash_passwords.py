from werkzeug.security import generate_password_hash
import pyperclip as pc

'''
Here you can hash your master password, just run this python file and enter the requested information
then the hashed password will be copied to your clipboard and you will be able to change the hashed_password
content in the app_menu.py file.
'''

password = input('Enter the password you want to hash => ')
hashed_password = generate_password_hash(password)
pc.copy(hashed_password)
print('The hashed password has been copied to your clipboard.')
print('Now, you can modify the hashed_password variable on the app_menu.py file.')