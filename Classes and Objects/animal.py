class Animal:

    def __init__(self, breed = None, name = None, size = None, age = None, temperament = None):
        # as fas as database table is concerned, the following are either fields, attributes or columns
        self.breed = breed
        self.name = name
        self.size = size 
        self.age = age 
        self.temperament = temperament
    
    

    def setBreed(self, breed):
        self.breed = breed
    
    def getBreed(self):
        return self.breed 

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setSize(self, size):
        self.size = size
    
    def getSize(self):
        return self.size 
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age 

    def setTemperament(self, temperament):
        self.temperament = temperament
    
    def getTemperament(self):
        return self.temperament 


    
