import os, time
os.system('clear')

# A CUSTOM function can take as many arguments as you want 
def calculate(n1, n2):
    sum = n1 + n2
    print(f'The sum of {n1} and {n2} is {sum}')
    # age = 44
    # **** THREE DIFFERENT WAYS TO PRINT IN PYTHON ******** 
    # print('I am', age, 'years old')
    # print(f'I am {age} years old')
    # print('I am {} years old'.format(age))


while True:
    num1 = int(input('Enter a number >> '))
    num2 = int(input('Enter another number >> '))
    calculate(num1, num2)
    response = input('Do you want to enter other numbers? [Y/N] >> ')
    while True:
        if(response.upper() == 'Y' or response.upper() == 'N'):
            break
        else: 
           print('Invalid entry. Try again')
           response = input('Do you want to enter other numbers? [Y/N] >> ')
    if (response.upper() == 'N'):
        print('Thank you for using our humble calculator. Have a great day!!!!!! :)')
        break

print(' ')
print('************************  MORE ON FUNCTIONS ***************************')
def printText():
    print('Printing from this printText() function without any arguments')
printText()

def printAnotherText(text):
    print('Printing from this printAnotherText() function with text: ', text)
printAnotherText('I love you')

def returnText():
    return 'I am returning this value'
print(returnText()) # print('I am returning this value')
text = returnText() # text = 'I am returning this value'
print(text)
print('This is the text that I got:', text)



# calling a function without any arguments => function returns something
def add():
    addition = 4 + 6 # addition is a local variable
    return addition

print(add())
addition = add() # method call 
print(addition)

# calling a function with two arguments => function returns something
def calculateSub(num1, num2):
    subtraction = num1 - num2
    return subtraction

sub = calculateSub(3, 7)
print(sub)
print(calculateSub(3, 7))

# calling a function with arguments => function returns more than one value
def returnMultipleValue(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    modulus = num1 % num2
    return addition, subtraction, multiplication, division, modulus

add, sub, mul, div, mod = returnMultipleValue(3, 5)
print('''
     Addition:........... {}
     Subtraction:........ {}
     Multiplication...... {}
     Division............ {}
     Modulus............. {}
'''.format(add, sub, mul, div, mod))

print(returnMultipleValue(3, 5))

# Working with the scope of variables
x = 'fantastic' # outer world

def printLocal():
    x = 'awesome' # inner world
    print('Local x =', x) # inner world

printLocal()# outer world
print('Global x =', x) # outer world

def printOptionalArguments(num1 = None, num2 = None):
    if (num1 == None):
        num1 = int(input('I see you are not passing any number for num1. Enter a number >> '))
    if (num2 == None):
        num2 = int(input('I see you are not passing any number for num2. Enter another number >> '))
    addition = num1 + num2
    print('The sum of', num1, 'and', num2, 'is', addition)

os.system('clear')
print('Calling printOptionalArguments() for the first time')
time.sleep(5)
printOptionalArguments()
print(' ')
print('Calling printOptionalArguments(5, 7) for the second time, passing 5 and 7')
time.sleep(5)
printOptionalArguments(5, 7)
print(' ')
print('Calling printOptionalArguments(7) for the third time, passing 7 alone => it matches num1 in the function')
time.sleep(5)
printOptionalArguments(7)

