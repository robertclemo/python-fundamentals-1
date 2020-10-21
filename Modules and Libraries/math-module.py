import math
from math import pi, fabs, floor, ceil

print('The value of pi is', round(pi, 2))
number1 = -1
print('The absolute value of', number1,  'is',  fabs(number1)) # this returns the absolute value of -1 = 1.0
print('After converting', fabs(number1), 'into an integer, we get', int(fabs(-1))) # this returns the absolute value of -1 = 1.0 but converted to an int = 1

number2 = 3.7
print('The floor of', number2, 'is', floor(number2)) # returns The floor of 3.7 is 3
print('The ceiling of', number2, 'is', ceil(number2))# returns The ceiling of 3.7 is 4