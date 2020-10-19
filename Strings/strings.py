import os
os.system('clear')

print('This is simple quotes - \033[1;32;40m"Really?"') # => prints This is simple quotes - "Really?"
print("Double quotes inside \033[1;31;40m\"double\" quotes") # => prints Double quotes inside "double" quotes
print('Single quotes inside \033[1;33;40m\'single\' quotes') # => prints Single quotes inside 'single' quotes
print("It's is \033[1;34;40mdouble quotes") # => prints It's is double quotes
print('''This is \033[1;35;40mtriple quotes''') # => prints This is triple quotes