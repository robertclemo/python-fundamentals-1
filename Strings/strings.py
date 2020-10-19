import os
os.system('clear')

print('This is simple quotes - \033[1;32;40m"Really?"') # => prints This is simple quotes - "Really?"
print("Double quotes inside \033[1;31;40m\"double\" quotes") # => prints Double quotes inside "double" quotes
print('Single quotes inside \033[1;33;40m\'single\' quotes') # => prints Single quotes inside 'single' quotes
print("It's is \033[1;34;40mdouble quotes") # => prints It's is double quotes
print('''This is \033[1;35;40mtriple quotes''') # => prints This is triple quotes

name = "\033[0mRobert"
lname = "Clemo"
print(name + " " + lname) # => Concatenation = append strings => Robert Clemo


# \033[0m => this sets color to normal (regular)

# **** ASSIGNMENT ******
name1 = "Carlos" # => name = Carlos
name2 = name1 # name2 = Carlos
name3 = name2 # name3 = Carlos
# **** RE- ASSIGNMENT *******
name3 = 'Benito' # name3 = Benito
name1 = name3 # name1 = Benito
name2 = name1 # name2 = Benito
print(name2) # this returns Benito
print(name1)# this returns Benito
print(name3)# this returns Benito

name1 = "Pedro"
name4 = "Antonio"
name3 = "Carlos"
name2 = name3
name4 = name2
name1 = name4
print("What is the value of name4?") # => returns name4 is Carlos
print(f'name4 is {name4}')
print("What is the value of name1?") # => returns name1 is Carlos
print(f'name1 is {name1}')

apple = "4"
orange = "6"
print(apple + orange) # => strings => returns 46 = appleorange = 46

apple = "I am"
orange = "happy"
print(apple + orange) # => returns I amhappy

apple = int("4")
orange = int("6")
print(apple + orange) # => (integers) 4 + 6 => returns 10
weirdText = "lAJELajdlajlkdlkaDLKajdj 293498237498723894789237 122232323222@@@@@@@@@??????//////////"
print(weirdText + "This is really weird") # => concatenating strings
# returns lAJELajdlajlkdlkaDLKajdj 293498237498723894789237 122232323222@@@@@@@@@??????//////////This is really weird

num1 = int("100")
num2 = int("50")
print(num1 + num2) #100 + 50 => 150, "100" + "50" => 10050 

print(type("100")) # returns <class 'str'>
print(type("50")) # returns <class 'str'>
print(type(100)) # returns <class 'int'>
print(type(True)) # returns <class 'bool'>
print(type(4.6)) # returns <class 'float'>

