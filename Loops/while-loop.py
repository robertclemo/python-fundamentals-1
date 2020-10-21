import os
os.system('clear')

counter = 0
hiCounter = 0
while counter < 10: # when counter = 10, then the boolean expression counter < 10 becomes false, then it exits the loop
    print(f"{hiCounter + 1}. Hi")
    counter+=1
    hiCounter+=1



attemptCounter = 3
while True:
    input('Login >> ') 
    if (attemptCounter == 1):
        break
    print(f"You have {attemptCounter - 1} attempts")
    attemptCounter -= 1

os.system('clear')
while True:
    num = int(input('Enter a number between 1 and 3 >> '))
    if (num >= 1 and num <= 3):
        print('Valid Entry')
        break
   

people = []
namesCounter = 0

os.system('clear')
names = int(input('How many full names do you want to add to the roster? >> ')) 

listCounter = 1
while namesCounter < names:
    print('******************************')
    print(f'Enter full name # {listCounter}')
    fname = input('Enter your first name >> ')
    lname = input('Enter your last name >> ')
    price = float(input('Enter a price >> '))
    fullName = fname + " " + lname + " - $" + str(price) 
    people.append(fullName)
    namesCounter += 1
    listCounter += 1


nameListCounter = 1
for person in people:
    print(f'''
     {nameListCounter}. {person}''')
    nameListCounter += 1


while True:
    print('Hello')
    break;


# num = 10
# while num > 10:
#     print("HHHHHHHHHHHHHHHHHH") => This will never execute because the boolean num > 10 is always false



