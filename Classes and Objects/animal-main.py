import os
from os import system 
from animal import Animal


system('clear')

animalList = []
number_of_animals = int(input('How many animals do you want to create? >> '))
print(f'Nice!!, {number_of_animals} animals')
print('Here we go!!')

for a in range(number_of_animals):
    animal = Animal()
    print(f"*** Animal # {a + 1} ***")
    breed = str(input('What is the breed of your animal? >> '))
    animal.setBreed(breed)
    name = str(input('What is the name of your animal? >> '))
    animal.setName(name)
    size = float(input('What is the size of your animal? >> '))
    animal.setSize(size)
    age = int(input('What is the age of your animal? >> '))
    animal.setName(name)
    temperament = str(input('What is the temperament of your animal? >> '))
    animal.setTemperament(temperament)
    animalList.append(animal)

for animal in animalList:

    print(f'''
        Breed:............ {animal.getBreed()}
        Name:............. {animal.getName()}
        Size:............. {animal.getSize()}
        Age:.............. {animal.getAge()}
        Temperament....... {animal.getTemperament()}
    
    ''')

    params = {'a': 1, 'b': 2}
    a, b = params.values()

    print(a, b)



    

