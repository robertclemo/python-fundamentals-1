import os
from os import mkdir, listdir, system, getcwd, getenv, getlogin

#mkdir('My Directories')

print('')
print('****** List of Directories and Files *******')
directories = listdir()
print(directories)
#print(listdir()) => returns the same output as line 9
print('')
print('****** Current Working Directory *******')
cwd = getcwd()
print(cwd)
#print(getcwd()) => returns the same output as line 14
print('')
print('****** List of Directories and Files including permissions *******')
listOfDirectoriesAndFiles = system('ls -lah')
print(listOfDirectoriesAndFiles)
#print(system('ls -lah')) => returns the same output as line 19
print('')
print('****** Logged-in User *******')
user = getlogin()
print(user)
#print(getlogin()) => returns the same output as line 24

print('')
print('****** Printing the USER environment variable *******')
user = getenv('USER')
print(user)
#print(getenv('USER')) => returns the same output as line 30
print('')
print('****** Printing the PATH environment variable *******')
path = getenv('PATH')
print(path)
#print(getenv('PATH')) => returns the same output as line 35
print('')
print('****** Printing the SHELL environment variable *******')
shell = getenv('SHELL')
print(shell)
#print(getenv('SHELL')) => returns the same output as line 40
print('')
print('****** Printing the PWD environment variable *******')
pwd = getenv('PWD')
print(pwd)
#print(getenv('PWD')) => returns the same output as line 45
