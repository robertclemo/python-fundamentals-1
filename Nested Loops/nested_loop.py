teams = "Team 1, Team 2, Team 3"
names = "Julio, Pablo, Dunieski, Kristy, Carlos, Christian, David, Daniel, Dennire, Desire, Lanise, Nahomie"
teamsList = teams.split(", ")
counter = 0
print()
for team in teamsList:
    print("--------")
    print(f"{team}: ")
    print("--------")
    for n in range(4):
        namesList = names.split(", ")
        print(namesList[counter])
        counter += 1
        print()