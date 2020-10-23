import json, os
from json import dumps, loads
from os import system

system('clear')

# this will change a number to a string
num = 15
result = dumps(num)
print(f'{result} has type: {type(result)}')


# this will change a string to a number
myString = '56'
result = loads(myString)
print(f'{myString} has type: {type(result)}')

