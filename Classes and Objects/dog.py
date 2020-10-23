class Dog:

    def bark(self, name):
        print(f'{name} can bark')
    
    def fetch(self, name):
        print(f'{name} can fetch')

    def pee(self, name):
        print(f'{name} can pee')
    
    def sit(self, name):
        print(f'{name} can sit')
    
    def run(self, name):
        print(f'{name} can run')
    

    def calculateAge(self, name, dogAge):
        age = dogAge * 7
        print(f'Based on what the public says, {name} is {age} years old')
