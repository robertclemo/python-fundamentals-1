import math, time
import os
os.system('clear')

print(3 ** 2) # exponentiation => 3 elevated to the power of 2

print(10//3) # => floor of 10/3

x = 10/3
flr = math.floor(x)
cl = math.ceil(x)
print(flr)
print(cl)

flr = math.floor(4.6)
cl = math.ceil(4.6)
print(flr)
print(cl)


liters = 12.5
gallons = 12.5 / 3.7
print(f"How many gallons do I need? Well, after careful consideration and having {liters} liters, I have come to realized that...")
print('THINKING NOW.....', end='\r')
time.sleep(4)
#foreground
print("\033[1;31;40mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;32;40mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;33;40mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;34;40mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;35;40mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;36;40mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;37;40mI need {} gallons".format(int(math.ceil(gallons))))
# background
print("\033[1;37;40mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;30;41mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;30;42mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;30;43mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;30;44mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;30;45mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;30;46mI need {} gallons".format(int(math.ceil(gallons))))
print("\033[1;30;47mI need {} gallons".format(int(math.ceil(gallons))))