def get_classA_price():
    #check variable type
    try:
        tickets = int(input("How many class A tickets did you sell? "))
        price = 20 * tickets 
        return price
    except ValueError:
        print("Please enter a valid number")
        get_classA_price()

def get_classB_price():
    #check variable type
    try:
        tickets = int(input("How many class B tickets did you sell? "))
        price = 15 * tickets 
        return price
    except ValueError:
        print("Please enter a valid number")
        get_classB_price()

def get_classC_price():
    #check variable type
    try:
        tickets = int(input("How many class C tickets did you sell? "))
        price = 10 * tickets 
        return price
    except ValueError:
        print("Please enter a valid number")
        get_classC_price()

def main():
    classA_price = get_classA_price()
    classB_price = get_classB_price()
    classC_price = get_classC_price()

    total_price = classA_price + classB_price + classC_price

    print(f"Total price of tickets: {total_price:.2f}")

main()