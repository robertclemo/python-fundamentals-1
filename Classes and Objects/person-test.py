from person import Person 


person1 = Person()
person2 = Person()
person3 = Person()
person4 = Person("Carlos")

person1.setFName("Dunieski")
person2.setFName("Orlando")
person3.setFName("Connor")

print("Person 1: ", person1.getFName())
print("Person 2: ", person2.getFName())
print("Person 3: ", person3.getFName())
print("Person 4: ", person4.getFName())