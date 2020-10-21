import json

datastore= []
with open('users.json', 'r') as files:
    datastore = json.load(files)

for data in datastore:
    print(f"""
    Hello, {data['name']}, 
    This is the information we have about you:
    Name: {data['name']} 
    Age: {data['age']}
    Education Level: {data['Educational_Level']}
    SSN: {data['SSN']}""")

   # THE ABOVE WILL PRINT THE FOLLOWING:
    # Hello, Dunieski, 
    # This is the information we have about you:
    # Name: Dunieski 
    # Age: 44
    # Education Level: Master's Degree
    # SSN: 123456789

    # Hello, Orlando, 
    # This is the information we have about you:
    # Name: Orlando 
    # Age: 36
    # Education Level: Master's Degree
    # SSN: 123456789

    # Hello, Martha, 
    # This is the information we have about you:
    # Name: Martha 
    # Age: 56
    # Education Level: Master's Degree
    # SSN: 123456789