import os
os.system('clear')

num = 4.6
print(num)
print(type(num))

num1 = int(num)
print(num1)
print(type(num1))


num2 = float(num1)
print(num2)
print(type(num2))


myString = str(num2)
print(myString)
print(type(myString))


myBoolean = True
print(myBoolean)
print(type(myBoolean))

if(type(num) == 'int'):
    print('OK')
else:
    print('Enter an integer >> ')