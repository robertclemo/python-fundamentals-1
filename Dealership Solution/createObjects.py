from car import Car 

def createObject(make, model, year, color):
    car = Car()
    car.setMake(make)
    car.setModel(model)
    car.setYear(year)
    car.setColor(color)
    return car 