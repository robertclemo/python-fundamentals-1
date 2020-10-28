from car import Car 
import colorama
from colorama import Fore, Back, Style

def createObject(make, model, year, color, originalPrice, totalPrice, bonus, additionalDiscount):
    car = Car()
    car.setMake(make)
    car.setModel(model)
    car.setYear(year)
    car.setColor(color)
    car.setOriginalPrice(originalPrice)
    car.setTotalPrice(totalPrice)
    car.setBonus(bonus)
    car.setAdditionalDiscount(additionalDiscount)
    return car 


def calculateTotalPrice(price, color, warVetOrDisable):
    bonus = 0
    totalPrice = 0
    additionalDiscount = 0
    subtotal = 0
    taxes = .07
    if(str.upper(color) == "BLACK" and warVetOrDisable == False):
        additionalDiscount = price*.25
        subtotal = price-additionalDiscount
        totalPrice =  subtotal + (subtotal * taxes)
        print(
            f"As you chose {color}, you have a discount of 25% which is ${additionalDiscount} ")

    elif(str.upper(color) == "BLACK" and warVetOrDisable):
        bonus = 500
        additionalDiscount = price*.25
        subtotal = price - bonus - additionalDiscount
        totalPrice =  subtotal + (subtotal * taxes)
        print(Fore.YELLOW, f'''
        As you chose {color}, you have a discount of 25% which is ${additionalDiscount} 
        and as you are a veteran or disabled you get an extra bonus of ${bonus}''')

    elif(str.upper(color) == "WHITE" and warVetOrDisable == False):
        bonus = 400
        subtotal = price - 400
        totalPrice =  subtotal + (subtotal * taxes)
        print(Fore.YELLOW, f"As you chose {color}, you have a discount of ${bonus}")
        print(Style.RESET_ALL)

    elif(str.upper(color) == "WHITE" and warVetOrDisable):
        bonus = 500
        additionalDiscount = price * .25
        subtotal= price - bonus - additionalDiscount
        totalPrice =  subtotal + (subtotal * taxes)
        print(Fore.YELLOW, f'''
        As you chose {color}, you have a discount of ${bonus} 
        and as you are a veteran or disabled you get an extra 25% off which is ${additionalDiscount}''')
        print(Style.RESET_ALL)
    else:
        totalPrice = price + (price * taxes)
    return totalPrice, bonus, additionalDiscount


def checkInventory(value, collection):
    field = str(input(f'What is the {value}? >> '))
    print(field.capitalize())
    print(field.upper())
    while True:
        if(field.upper() not in collection):
            print(f'{value} is not found in our records. Please try again')
            field = str(input('What is the make? >> ')) 
        else:
            break            
    return field