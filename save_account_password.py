#! python

'''This is the program to store your accounts password.'''

import sys
import pyperclip

stored_password = {
    'instagram': 'mountain878756',
    'facebook': 'river457634',
    'email': 'skyisthelimit4563',
    'netflix': 'bingewatchagain678946'
}

if len(sys.argv) < 2:
    print("This program will copy the accout password which you have saved!")
    print("Typer in this manner to copy password-python pwlocker.py accountname")
    sys.exit()


account = sys.argv[1]
if account in stored_password:
    pyperclip.copy(stored_password[account])
    print(
        f"The password of your {account} account has been copied to clip board!")
else:
    print(f"Ther is no {account} account's password is stored!")
