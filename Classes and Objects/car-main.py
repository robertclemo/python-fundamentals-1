
from vehicle import Vehicle
import os, math
from os import system
from math import pi 

system('clear')

bwm = Vehicle()
bwm.run()
bwm.park()
bwm.speed()
bwm.stop()
bwm.turn()

name = str(input('Please enter your name >> '))
bwm.printName(name)

result = bwm.calculate(round(pi, 2), 12)
print(f'Result = {result}')
#print(bwm.calculate(round(pi, 2), 12)) => less efficient
