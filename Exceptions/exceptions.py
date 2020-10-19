import os
os.system('clear')

num1 = int(input('Enter a number >> '))
num2 = int(input('Enter another number >> '))

try:
    division = round(num1 / num2, 2)
    print('division = {}'.format(division))
except ZeroDivisionError: print(f'Division by {num2} is allowed')


try:
    num = int(input('Enter a number >> '))
    print(f'You entered {num}')
except ValueError: int(input('Invalid type. Try again >> '))