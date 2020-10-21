import os, datetime
from os import system
from datetime import datetime

username = 'dunieski'
password = 'pass'

user = input('Enter your username >> ')
passwd = input('Enter your password >> ')

def printSuccessOrNot(message):
    if (message == 'Success'):
        with open('log.txt', 'a') as log:
            log.write(f'\nUser {user} logged in on {datetime.now()} - Result: {message}')
            log.close
    else:
        with open('log.txt', 'a') as log:
            log.write(f'\nUser {user} logged in on {datetime.now()} - Result: {message}')
            log.close


if(user == username and passwd == password):
    print(f'Hello, {user}, you are fully authenticated')
    printSuccessOrNot('Success')
else:
    print(f'The combination of the username and password you used does not match our records')
    printSuccessOrNot('Failure')

   