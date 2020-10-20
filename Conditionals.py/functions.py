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