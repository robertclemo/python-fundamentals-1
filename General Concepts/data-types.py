import os 

os.system('clear')

myNumber = 1
myFloat = 2.5
myBoolean = True
myString = 'My Class'

print(f'''\033[1;32;40m
   myNumber....... {myNumber}
   myFloat........ {myFloat}
   myBoolean...... {myBoolean}
   myString....... {myString}
''')

print('''
   myNumber....... {}
   myFloat........ {}
   myBoolean...... {}
   myString....... {}
'''.format(myNumber, myFloat, myBoolean, myString))










