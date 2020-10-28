import os, time
os.system('clear')
hasABadge = False
response = 0

print('Hey Luke, there is a guys coming to our office. Check if he has a badge!!')
print('Checking now...', end='\r')
time.sleep(4)
print("I've got it")
response = int(input('So does he have it (1 for Yes, 2 for No, or 3 for surprised)? >> '))

if (response == 1):
    hasABadge = True
elif (response == 2):
    hasABadge    
else:
    print("What? That guy is the CEO. I am not going to mess with him. I don't want to be fired")

if (hasABadge):
    print('Perfect. Always checking compliance')
else:
    print('Please tell him to wear a badge')