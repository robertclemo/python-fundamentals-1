import os
os.system('clear')

# reverse() => it reverses the list
# copy() => it copies the list to another list
# append() => it appends info/elements to the list
# insert() => it inserts elements to a list at a specific index ('index', 'element') => it takes two arguments
# remove() => it removes a specific element from the list => takes 1 argument => remove('element')
# pop() => it removes the last element of the list
# sort() => it sorts the list
# count() => it counts a particular element in the list => takes one argument => count('element')
# clear() => it clears the list 

numbers = [ 3, 4, 5, 6, 2, 1, 9, 2, 0]
numbers1 = numbers.copy()
print('')
print('******** USING THE reverse() METHOD *********')
print('List without yet invoking the reverse() method: \n{}'.format(numbers))
numbers.reverse()
print('List without after invoking the insert() method: \n{}'.format(numbers))
print('******************************************')
print('')
print('******** USING THE copy() METHOD *********')
print('First list: \n{}'.format(numbers))
print('New list numbers1: \n{}'.format(numbers1))
print('******************************************')
print('')
numbers.append(15)
print('******** USING THE append() METHOD *********')
print('List with 15 added: \n{}'.format(numbers))
print('********************************************')
print('')
print('******** USING THE insert() METHOD *********')
print('List without yet invoking the insert() method: \n{}'.format(numbers))
#number.insert('index', 'value')
numbers.insert(2, 20)
print('List after invoking the insert() method: \n{}'.format(numbers))
print(' ')
print('******** USING THE remove() METHOD *********')
print('List without yet invoking the remove() method: \n{}'.format(numbers))
#number.insert('index', 'value')
numbers.remove(20)
print('List after invoking the method() method: \n{}'.format(numbers))
print(' ')
print('******** USING THE pop() METHOD *********')
print('List without yet invoking the pop() method: \n{}'.format(numbers))
numbers.pop()
print('List after invoking the pop() method: \n{}'.format(numbers))
print('********************************************')
print(' ')
print('******** USING THE sort() METHOD *********')
print('Unsorted list: \n{}'.format(numbers))
numbers.sort()
print('Sorted list: \n{}'.format(numbers))
print('********************************************')
print(' ')
print('******** USING THE count() METHOD *********')
print('{}'.format(numbers))
for number in numbers:
    print('{} is repeated {} times'.format(number, numbers.count(number)))
print('********************************************')
print(' ')
print('******** USING THE clear() METHOD *********')
print('List without yet invoking the clear() method: \n{}'.format(numbers))
numbers.clear()
print('List after the clear() method: \n{}'.format(numbers))
print('********************************************')







  