import json

datastore = []
with open('log.json', 'r') as files:
    datastore = json.load(files)

for n in datastore:
    print(f"Hello, {n['name']}, you are {n['age']} years old\n and your education level is {n['Education_Level']} and your SSN is {n['SSN']}")


def demo(x):
    print(x)


def demo(x, y):
    print(x, y)


def demo(x, y, z):
    print(x, y, z)


demo(5)
demo(5, 4)
demo(5, 6, 7)
