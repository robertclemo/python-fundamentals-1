from package import Package
import os
from os import system
system('clear')

packageList=[]

numberPackages = int(input('How many packages are you bringing? >> '))

for i in range(numberPackages):
    package = Package()
    package.setLength(float(input('Enter length >> ')))
    package.setWidth(float(input('Enter width >> ')))
    package.setHeight(float(input('Enter height >> ')))
    package.setWeight(float(input('Enter weight >> ')))
    packageList.append(package)

for package in packageList:
    print(f'''    
        Length: {package.getLength()}
        Width:  {package.getWidth()}
        Height: {package.getHeight()}
        Weight: {package.getWeight()}
    ''')