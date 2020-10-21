import os
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