def collect_input():
    rent = input("Enter your monthly rent expense: ")
    gas = input("Enter your monthly gas expense: ")
    food = input("Enter your monthly food expense: ")
    clothing = input("Enter your monthly clothing expense: ")
    car = input("Enter your monthly car expense: ")

    writeFile(rent, gas, food, clothing, car)

def writeFile(rent, gas, food, clothing, car):
    output_file = open("./Week8/Midterm/monthlyexpenses.txt", "w")

    output_file.write(f"Monthly Expenses\nRent: ${rent}\nGas: ${gas}\nFood: ${food}\nClothing: ${clothing}\nCar: ${car}")
    print('Your file monthlyexpenses.txt was created.')

def readFile():
    input_file = open("./Week8/Midterm/monthlyexpenses.txt", "r")
    
    for line in input_file:
        print(line)

collect_input()
readFile()