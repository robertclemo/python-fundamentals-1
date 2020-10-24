from colorama import Fore, Back, Style

print(Fore.RED, "Text in Red")
print(Back.GREEN, Fore.BLACK, "and with a green background")
print(Style.DIM,  "and in dim text")
print(Style.RESET_ALL)
print(Style.NORMAL, 'back to normal')
print(Style.RESET_ALL, 'back to normal')