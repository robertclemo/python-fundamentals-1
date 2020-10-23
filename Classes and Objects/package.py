class Package:

    def __init__(self, length = None, width = None, height = None, weight = None):
        self.length = length
        self.width = width 
        self.height = height
        self.weight = weight 

    
    def setLength(self, l):
        self.length = l 
    
    def getLength(self):
        return self.length
    
    def setWidth(self, w):
        self.width = w
    
    def getWidth(self):
        return self.width
    
    def setHeight(self, h):
        self.height = h 
    
    def getHeight(self):
        return self.height
    
    def setWeight(self, we):
        self.weight = we
    
    def getWeight(self):
        return self.weight