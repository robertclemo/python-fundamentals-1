class Vehicle:

    def run(self):
        print("I run")

    def speed(self):
        print("I move fast")
    
    def stop(self):
        print("I can stop")

    def park(self):
        print("I can park")

    def turn(self):
        print("I run")
    
    def printName(self, name = None):
        print(f'Hello, {name}')
    
    def calculate(self, pi, num):
        result = pi * num
        return result