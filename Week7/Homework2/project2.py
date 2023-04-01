LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    produce = get_initial_dict()

    for key,value in produce.items():
        print(key + ": $" + value)

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(produce)
        elif choice == ADD:
            add(produce)
        elif choice == CHANGE:
            change(produce)
        elif choice == DELETE:
            delete(produce)

    if choice == QUIT:
        write_output_file(produce)

def get_menu_choice():
    print()
    print('Pickled Vegetables')
    print('------------------------------')
    print('1. See list of vegetables')
    print('2. Add a vegetable')
    print('3. Change price of a vegetable')
    print('4. Delete a vegetable')
    print('5. Quit the program')
    print()
    
    choice = int(input('Enter your choice: '))
    while choice < LOOK_UP or choice > QUIT:
        print('Enter a valid choice: ')
    return choice

def delete(produce):
    name = input("Enter a vegetable: ")

    if name in produce:
        del produce[name]
        for key,value in produce.items():
            print(key + ": $" + value)
    else:
        print('That vegetable is not found')


def change(produce):
    name = input("Enter a vegetable: ")

    if name in produce:
        new_price = input(f"What is the new price of {name}: ")
        produce[name] = new_price
        for key,value in produce.items():
            print(key + ": $" + value)
    else:
        print('That vegetable is not found')

def add(produce):
    name = input("Enter a vegetable: ")
    new_price = input(f"What is the price of {name}: ")
    produce[name] = new_price
    for key,value in produce.items():
        print(key + ": $" + value)

def look_up(produce):
    for key,value in produce.items():
        print(key + ": $" + value)

def get_initial_dict():
    input_file = open("Week7/Homework2/vegetables.data", "r")
    
    produce = {}

    for line in input_file:
        new_line = line.rstrip('\n')
        key_value = new_line.split(":")
        produce[key_value[0]] = key_value[1]
    
    input_file.close()

    return produce

def write_output_file(produce):
    output_file = open("Week7/Homework2/vegetables.data", "w")
    for key,value in produce.items():
        output_file.write(key + ":" + value + "\n")
    
    output_file.close()

if __name__ == '__main__':
    main()