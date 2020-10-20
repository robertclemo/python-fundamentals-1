import os
os.system('clear')

myNewDisctionary = {
    "Integer": 4,
    "Float": 3.6,
    "String": "I am here",
    "Boolean": True,
    "FirstName": "Jorge",
    "LastName": 'Martinez', 
    "Age": 79
}

print(myNewDisctionary)
# Print first element:

print(f'First Element: {myNewDisctionary["Integer"]}')

# Print every element of the dictionary

keys = myNewDisctionary.keys() # this will get the keys
values = myNewDisctionary.values() # this will get the values
print(f'{keys} - {values}')


print(keys)
for element in myNewDisctionary:
    print(f' - {myNewDisctionary[element]}')

for element in myNewDisctionary:
    print(myNewDisctionary.get(element))


# Prints key and value from Dictionary
for i in myNewDisctionary:
    print(i, myNewDisctionary[i])

# Prints key and value from Dictionary
for key, value in myNewDisctionary.items():
    print(f"\"{key}\": \"{value}\"")