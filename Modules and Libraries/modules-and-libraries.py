import os, math, time 
from os import system
from time import sleep 

# system()
# print()
# round()
# sleep()
# open()
# close()

system('clear')
sleep(2)
print('Good bye')

fileName = input('What do you want to name your file >> ')
extension = input('What extension do you want to use? (e.g. pdf, txt, py, cs, js..) >> ')
content = input('What content do you want to add to the file >> ')
file = fileName + "."+ extension
system(f'touch {file}')
system(f"echo '{content}' > {file}")

# this will read newFile.txt content
f = open(f'{file}', 'r')
content = f.read()
system('clear')
print(f"We are printing the content of {file}")
print(content) # prints content
f.close()

