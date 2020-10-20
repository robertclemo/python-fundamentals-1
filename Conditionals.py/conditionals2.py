import os
os.system('clear')

maxGallonQt = 15
lowGallonQt = 2
isARental = False # flag


def conditional_decided(currentStatus, lowGallonQt):
    if (currentStatus >= 12 and currentStatus <= 15):
        print("You are good, and I would probably say you're perfect")
    elif (currentStatus >= 3 and currentStatus <= 11):
        print('We think you should be thinking about some replenishment')
    elif (currentStatus > lowGallonQt and currentStatus < 3 ):
        print('My friend, you are about to start running on fumes')
    elif (currentStatus == lowGallonQt):
        print('Low fuel warning has been turned on')
    else:
        print('Oh my God, my car just stopped in the middle of the highway')


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
        conditional_decided(currentStatus, lowGallonQt)    
else:
    if (currentStatus < 0  or currentStatus > 15):
        print('Invalid entry. You have been automatically forgiven bc this is not your car. Please check again')
    else:
        conditional_decided(currentStatus, lowGallonQt) 

