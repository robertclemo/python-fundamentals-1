import os
from os import system
from dog import Dog 

system('clear')

poodle = Dog()
dogName = str(input("What is your dog's name? >> "))
dogAge = int(input("What is your dog's age? >> "))
poodle.bark(dogName)
poodle.fetch(dogName)
poodle.pee(dogName)
poodle.sit(dogName)
poodle.run(dogName)
poodle.calculateAge(dogName, dogAge)
