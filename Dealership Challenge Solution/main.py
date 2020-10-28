import os 
from os import system 
from data import *
import functions as func 
import colorama
from colorama import Fore, Back, Style

system('clear')

carCounterPrint = 1
carCount = 1
carList = []
warVetOrDisabled = False
grandTotal = 0
totalDiscounts = 0
totalBonuses = 0

user = str(input('What is your name so that we can address you properly? >> '))
print(' ')
print('********* WELCOME TO NCI DEALERSHIP *********')
print(f'Hi, {user}')
print('These are the options we have available for you: ')

length = len(carInventoryList)
print(length)
for e in range(length):
    print(f'{carInventoryList[e]}        - {carColors[e]}      - ${carBasePrices[e]}')
amount_of_cars = int(input('How many cars do you want to purchase? >> '))
print(f'{amount_of_cars} cars. Cool. Let us do it!!!')


for i in range(amount_of_cars):
    print('')
    print(Fore.CYAN, f'Car # {carCount}: ')
    print(Style.RESET_ALL)
    make = func.checkInventory('make', carInventoryList)
    model = func.checkInventory('model', carModels)
    year = func.checkInventory('year', carYears)
    color = func.checkInventory('color', carColors)
    wVOrD = str(input('Are you a veteratan [Y/N]? >> '))
        
    if(wVOrD.upper() == 'Y'):
        warVetOrDisabled = True
    if(str.upper(make) == 'BMW'):
        originalPrice = carBasePrices[0]
        totalPrice, bonus, additionalDiscount = func.calculateTotalPrice(originalPrice, color, warVetOrDisabled)
    elif(str.upper(make) == 'MERCEDES'):
        originalPrice = carBasePrices[1]
        totalPrice, bonus, additionalDiscount = func.calculateTotalPrice(originalPrice, color, warVetOrDisabled)
    elif(str.upper(make) == 'TOYOTA'):
        originalPrice = carBasePrices[2]
        totalPrice, bonus, additionalDiscount = func.calculateTotalPrice(originalPrice, color, warVetOrDisabled)
    elif(str.upper(make) == 'NISSAN'):
        originalPrice = carBasePrices[3]
        totalPrice, bonus, additionalDiscount = func.calculateTotalPrice(originalPrice, color, warVetOrDisabled)
    elif(str.upper(make) == 'NISSAN'):
        originalPrice = carBasePrices[4]
        totalPrice, bonus, additionalDiscount = func.calculateTotalPrice(originalPrice, color, warVetOrDisabled)
    else:
        print(f'{make} is not found in our records. Please try again')
        break
        

    car = func.createObject(make, model, year, color, originalPrice, totalPrice, bonus, additionalDiscount)
    carCount+=1
    carList.append(car)
    

print("\n")
print(
        Fore.RED, f'''        ***** ORDER SUMMARY *****{Style.RESET_ALL}''')

for c in carList:
    print(Fore.BLUE, f'''
    Car # {carCounterPrint}''')
    print(Fore.GREEN, f'''
    Make........................ {c.getMake()}
    Model....................... {c.getModel()}
    Year........................ {c.getYear()}
    Color....................... {c.getColor()}
    Original Price.............. ${round(c.getOriginalPrice(), 2)}
    Bonus....................... ${c.getBonus()}
    Additional Discounts........ ${round(c.getAdditionalDiscount(),2)}
    Total Price................. ${round(c.getTotalPrice(), 2)}''')
    grandTotal += c.getTotalPrice()
    totalDiscounts += c.getAdditionalDiscount()
    totalBonuses += c.getBonus()
    carCounterPrint += 1

print(Fore.BLACK)
print(Back.WHITE)
print(f'Total Bonuses......... ${round(totalBonuses, 2)}')
print(f'Total Discounts...... ${round(totalDiscounts, 2)}')
print(f'GRAND TOTAL........... ${round(grandTotal, 2)}')