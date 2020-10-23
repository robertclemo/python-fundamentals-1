
class Person:
    # Constructor
    def __init__(self, fname = None, lname = None, age = None, phone = None, ssn = None):
        self.fname = fname 
        self.lname = lname
        self.age = age
        self.phone = phone
        self.ssn = ssn 
    
    # Getters and Setters
    def setFName(self, fname):
        self.fname = fname
        
    def getFName(self):
        return self.fname

    def setLName(self, lname):
        self.lname = lname         

    def getLName(self):
        return self.lname

    def setAge(self, age):
        self.age = age       

    def getAge(self):
        return self.age

    def setPhone(self, phone):
        self.phone = phone        

    def getPhone(self):
        return self.phone

    def setSSN(self, ssn):
        self.ssn = ssn         

    def getSSN(self):
        return self.ssn
    
