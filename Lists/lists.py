import os
os.system('clear')

computers = ['Toshiba', 'Dell', 'MacBook Pro', 'iMac', 'HP', 'Microsoft']
print(computers)

for computer in computers:
    print(computer)



# Both team members are printed

team1 = ['Blaine', 'Connor', 'Arthur', 'Woodson', 'Jeffery']
team2 = ['Christie', 'Essie', 'Robert', 'Megan', 'Ryan', 'Marshall']
team3 = ['Carlos', 'Benito', 'Yanet', 'Stephanie', 'Brian', 'Stanley']

teamCounter = 1

def printTeam(team):
    for member in team:
        print(f'\033[0;35;40m{member}')
        

for team in range(3):
    print('\033[0;31;40mTeam' + f' # {teamCounter}\033[33')
    if teamCounter == 1:
        printTeam(team1)
    elif teamCounter == 2:
        printTeam(team2)
    else:
        printTeam(team3)
    print('')
    teamCounter+=1

    
    

myList = ["a", "b", "c"]
#By using the destructuring syntax in the enumerate function below, we’re able to access elements in a way that’s more concise and easy to comprehend.
for i, element in enumerate(myList):
	print(i, element)


# you can ignore many values using the *_ syntax in the assignment:
a, *_, b = [1, 2, 3, 4, 5]
print(a, b)

# Prints: 1
a, *_ = [1, 2, 3, 4, 5]
print(a)
# Prints: 1