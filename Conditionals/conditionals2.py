import functions as func 
import os
os.system('clear')

maxGallonQt = 15
lowGallonQt = 2
isARental = False # flag

currentStatus = float(input('Please take a look at your gas gauge and tell us how many gallons do you have left? >> '))
response = int(input('Is this a rental? 1 for yes or 2 for no >> '))

if (response == 1):
    isARental = True
else:
    isARental

if (not isARental):
    if (currentStatus < 0 or currentStatus > 15):
        print(f'Invalid entry. Are you blind or do you just not know your car? Your car does not take more than {maxGallonQt} gallons. Please check the manual')
    else:
        func.conditional_decided(currentStatus, lowGallonQt)    
else:
    if (currentStatus < 0  or currentStatus > 15):
        print('Invalid entry. You have been automatically forgiven bc this is not your car. Please check again')
    else:
        func.conditional_decided(currentStatus, lowGallonQt) 

