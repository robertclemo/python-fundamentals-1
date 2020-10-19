import os
import random, time

os.system('clear')
print("6 > 5 = {}".format(6 > 5)) # => returns True
print("4 > 5 = {}".format(4 > 5)) # => returns False
print("10 >= 5 = {}".format(4 >= 5))# => returns False
print("5 >= 5 = {}".format(5 >= 5)) # => returns True
print("6 <= 5 = {}".format(6 <= 5)) # => returns False
print("6 != 5 = {}".format(6 != 5)) # => returns True  == equals, != not equals
print(not False) # => returns True

if (not(6 > 5)):
    print('true')
else: 
    print('not true')


num = 6

if (num > 0 and num < 10):
    print('bingo')
else:
    print('"un-bingo"')

num = random.randint(1, 5)
userNum = int(input('Enter a number >> '))

if (num == userNum):
    print(f'{num} == {userNum} => You just hit the dot')
else:
    print(f'{num} is not equal to {userNum}. Not lucky this time. Try again')

num = 0

username = input('Enter username >> ')
userNum = int(input('Enter a number >> '))

if (userNum >= 0 and userNum <= 20):
    print(f"{userNum} is between 0 and 20")
elif (userNum == 21 or userNum == 41):
    print("You are a winner")
elif (userNum == 45 or userNum == 65 and username == "Dunieski"):
    print(f'{username}, welcome')
else:
    print('Maybe next time')

# +=

num += 10 # => num = num + 10 => num = 0 + 10 => num = 10
print(f"Value of num is {num}")
# counter+=1 => increment => counter = counter + 1

# -=

print(f"Value of num is still {num}")
num -= 10 # => num = num - 10 => num = 10 - 10
print(num)

os.system('clear')
num1 = 10
print(f'current value of num1 is {num1}') # 10
num1 -= 1 # => num1 = 10 - 1

print('Doing the substraction now...', end='\r')
time.sleep(3)
print(f'The value of num1 is {num1}') # 9
time.sleep(3)

# *=
os.system('clear')
num1 = 8
print(f'current value of num1 is {num1} ')  
num1 *= 2 #  => num1 = num1 * 2 => 8 * 2 = 16

print('Doing the multiplication now...', end='\r') # 8
time.sleep(3)
print(f'The value of num1 is {num1} ')  # 16
time.sleep(4)

# /=
os.system('clear')
num1 = 8
print(f'current value of num1 is {num1} ')  
num1 /= 2 #   => num1 = num1 / 2 => 8 / 2 => 4

print('Doing the division now...', end='\r') # 8 
time.sleep(3)
print(f'The value of num1 is {int(num1)} ')  # 4 
time.sleep(4)
# %=
os.system('clear')
num1 = 10
print(f'current value of num1 is {num1} ')  
num1 %= 3 # => num = num1 % 3 => 10 % 3 => 10 /3 => remaind = 1

print('Doing the modulus now...', end='\r')  # 10
time.sleep(3)
print(f'The value of num1 is {int(num1)} ')  # 1

total = 10 / 5 * 2 # => returns 4 => 10 / 5 = 2, 2 * 2 = 4
total = 10 / (5 * 2) # => returns 1, 5 * 2 = 10 => 10/10 => 1
total = 10 * 5 / 2 # => returns 25, 10 * 5 = 50, 50 / 2 = 25
print(f'total is {total}')# => prints total is 25