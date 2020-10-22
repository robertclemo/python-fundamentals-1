
services = ["Oil Change", "Tire Rotation", "Battery Check", "Brake Inspection"]
servicesPrices = [25.99, 22.99, 15.99, 5.99]
servicesList = []

subtotal = 0
taxCal = 0
grandTotal = 0
taxes = .07
amountOil = 0
amountTir = 0
amountBat = 0
amountBra = 0

print("\033[1;34;40mThese are the services we have for you")

"""Hi"""
def calculateTotal(subtotal, price):
    subtotal = subtotal + price
    taxCal = subtotal * taxes
    grandTotal = subtotal + taxCal
    return subtotal, taxCal, grandTotal


while True:
    servicesCounter = 1
    for n in services:
        print(
            f"\033[1;35;40m{servicesCounter}. {n} -- ${servicesPrices[servicesCounter-1]}")
        servicesCounter += 1
    serviceChoice = input(
        "\033[1;33;40mWhat service would you like to choose ~ ")
    while True:
        if (str.upper(serviceChoice) == "OIL" or str.upper(serviceChoice) == "OIL CHANGE"):
            print(f"You have selected {services[0]}")
            servicesList.append(services[0])
            subtotal, taxCal, grandTotal = calculateTotal(
                subtotal, servicesPrices[0])
            amountOil += 1
            break
        elif(str.upper(serviceChoice) == "TIR" or str.upper(serviceChoice) == "TIRE ROTATION"):
            print(f"You have selected {services[1]}")
            servicesList.append(services[1])
            subtotal, taxCal, grandTotal = calculateTotal(
                subtotal, servicesPrices[1])
            amountTir += 1
            break
        elif(str.upper(serviceChoice) == "BAT" or str.upper(serviceChoice) == "BATTERY CHECK"):
            print(f"You have selected {services[2]}")
            servicesList.append(services[2])
            subtotal, taxCal, grandTotal = calculateTotal(
                subtotal, servicesPrices[2])
            amountBat += 1
            break
        elif(str.upper(serviceChoice) == "BRA" or str.upper(serviceChoice) == "BRAKE INSPECTION"):
            print(f"You have selected {services[3]}")
            servicesList.append(services[3])
            subtotal, taxCal, grandTotal = calculateTotal(
                subtotal, servicesPrices[3])
            amountBra += 1
            break
        else:
            print("Invalid choice. Try again")
            serviceChoice = input("What service would you like to choose ~ ")
    answer = input("do you want to add another services [Y/N] ~ ")
    if (str.upper(answer) == 'N'):
        break

print("\n\n\033[1;31;40m******* ORDER SUMMARY *******")
print("These are the services you have ordered: ")
for service in servicesList:
    print(f"\033[1;32;40m{service}")
print(f"\033[1;38;40mSubtotal.........${round(subtotal,2)}")
print(f"Taxes............${round(taxCal,2)}")
print(f"Grand Total.......${round(grandTotal,2)}\n\n")

print("""dasdljasdlajsdlasjdlsajdalsdjasldjalsdjasldjasdlajksd
dmalsdmaljdslasjdlasjdlasjdasldjasldjasldada
dlasdjasjd;askda;skdas;dkasd""")