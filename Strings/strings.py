import os
os.system('clear')

print('This is simple quotes - \033[1;32;40m"Really?"') # => prints This is simple quotes - "Really?"
print("Double quotes inside \033[1;31;40m\"double\" quotes") # => prints Double quotes inside "double" quotes
print('Single quotes inside \033[1;33;40m\'single\' quotes') # => prints Single quotes inside 'single' quotes
print("It's is \033[1;34;40mdouble quotes") # => prints It's is double quotes
print('''This is \033[1;35;40mtriple quotes''') # => prints This is triple quotes

name = "\033[0mRobert"
lname = "Clemo"
print(name + " " + lname) # => Concatenation = append strings


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