import os 
from os import system 
from data import *
import createObjects as create 

system('clear')

total = 0.0
discount = 0.0
subtotal = 0.0
taxes = .07
downpayment = 0.0
bonus = 0.0
originalPrice = 0.0
vetOrNotVet = ' '
bonusforVet = 0.0
taxesAmount = 0.0
carList = []

user = str(input('What is your name so that we can address you properly? >> '))
print(' ')
print('********* WELCOME TO NCI DEALERSHIP *********')
print(f'Hi, {user}')
print('These are the options we have available for you: ')

length = len(carInventoryList)
print(length)

for e in range(length):
    print(f'{carInventoryList[e]}        - {carColors[e]}      - ${carPrices[e]}')

amount_of_cars = int(input('How many cars do you want to purchase? >> '))

print(f'{amount_of_cars} cars. Cool. Let us do it!!!')


def calculateTotalPrice(colorPrice, color):
    bonus = 0.0
    discount = 0
    subtotal = 0
    taxesAmount =0
    total = 0
    bonusforVet = 0.00
    isVet = False
    vetOrNotVet = str(input('Are you a veteratan [Y/N]? >> '))
    
    if(vetOrNotVet.upper() == 'Y'):
        bonusforVet = 500
        isVet = True
    
    if(color == 'BLACK'):       
        downpayment = int(input('How much are putting down? >> '))
        if(isVet):
            discount = discount + (((colorPrice * .25) * .25) + downpayment + bonusforVet)
        else:
            discount = discount + ((colorPrice * .25) + downpayment)
        subtotal = subtotal + (colorPrice - discount )
        taxesAmount = taxesAmount + (subtotal * taxes)
        total = total + (subtotal  +  (subtotal * taxes))
    
    if(color == 'WHITE'):
        downpayment = int(input('How much are putting down? >> '))
        bonus = bonus + 400
        if(isVet):
            discount = discount + ((colorPrice * .25)  + downpayment + bonusforVet + bonus)
        else:
            discount = discount + ((colorPrice * .25) + downpayment + bonus)
        subtotal = subtotal + (colorPrice - discount)
        taxesAmount = taxesAmount + (subtotal * taxes)
        total = total + (subtotal  +  (subtotal * taxes))
    return colorPrice, vetOrNotVet, bonusforVet, discount, subtotal, taxes, taxesAmount, downpayment, bonus, total 


for i in range(amount_of_cars):
    make = str(input('What is the make? >> '))
    model = str(input('What is the model? >> '))
    year = int(input('What is the year? >> '))
    color = str(input('What is the color? >> '))
    if (str.upper(color) == 'BLACK'):
        originalPrice, vetOrNotVet, bonusforVet, discount, subtotal, taxes, taxesAmount, downpayment, bonus, total = calculateTotalPrice(carPrices[0], color.upper())
    if(str.upper(color) == 'WHITE'):
        originalPrice, vetOrNotVet, bonusforVet, discount, subtotal, taxes, taxesAmount, downpayment, bonus, total = calculateTotalPrice(carPrices[3], color.upper())
    car = create.createObject(make, model, year, color)
    carList.append(car)
     

for car in carList:
    print(f'''
    YOUR SELECTION:
    Make......{car.getMake()}
    Model......{car.getModel()}
    Year......{car.getYear()}
    Color......{car.getColor()}
    ''')
print(f'''
    ******* ORDER SUMMARY ********
    Veteran.............. {vetOrNotVet.upper()}
    Veteran Bonus........${bonusforVet}
    Original Price.......${originalPrice}    
    Downpayment......... ${downpayment}
    Color Bonus .........${bonus}
    Discount............ ${round(discount, 2)}
    Taxes............... % {taxes} = {round(taxesAmount, 2)}
    Subtotal............ ${round(subtotal, 2)}
    Grand Total......... ${round(total, 2)}''')
    



