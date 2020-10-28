class Car:

    def __init__(self, make=None, model=None, year=None, color=None, orginalPrice = None, totalPrice=None, bonus=None, additionalDiscount=None):
        self.make = make
        self.model = model
        self.year = year
        self.totalPrice = totalPrice
        self.bonus = bonus
        self.additionalDiscount = additionalDiscount
        

    def setMake(self, make):
        self.make = make 
    
    def getMake(self):
        return self.make 

    
    def setModel(self, model):
        self.model = model 
    
    def getModel(self):
        return self.model 

    def setYear(self, year):
        self.year = year
    
    def getYear(self):
        return self.year

    def setColor(self, color):
        self.color = color 
    
    def getColor(self):
        return self.color

    def setOriginalPrice(self, originalPrice):
        self.originalPrice = originalPrice 
    
    def getOriginalPrice(self):
        return self.originalPrice
    
    def setTotalPrice(self, totalPrice):
        self.totalPrice = totalPrice
    
    def getTotalPrice(self):
        return self.totalPrice
    
    def setBonus(self, bonus):
        self.bonus = bonus
    
    def getBonus(self):
        return self.bonus
    
    def setAdditionalDiscount(self, additionalDiscount):
        self.additionalDiscount = additionalDiscount 
    
    def getAdditionalDiscount(self):
        return self.additionalDiscount
