LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    birthdays = {"Kevin": "04/21/1998", "Isaac": "01/27/2010", "Janet": "12/13/1966"}
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('------------------------------')
    print('1. Look up a birthday')
    print('2. Add a birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()
    
    choice = int(input('Enter your choice: '))
    while choice < LOOK_UP or choice > QUIT:
        print('Enter a valid choice: ')
    return choice

def delete(birthdays):
    name = input("Enter a name: ")

    if name in birthdays:
        del birthdays[name]
        print(birthdays)
    else:
        print('That name is not found')


def change(birthdays):
    name = input("Enter a name: ")

    if name in birthdays:
        new_bday = input("Enter a new birthday: ")
        birthdays[name] = new_bday
        print(birthdays)
    else:
        print('That name is not found')

def add(birthdays):
    name = input("Enter a name: ")
    new_bday = input("Enter a birthday: ")
    birthdays[name] = new_bday
    print(birthdays)

def look_up(birthdays):
    name = input("Enter a name: ")

    if name in birthdays:
        print(birthdays[name])
    else:
        print('That name is not found')

if __name__ == '__main__':
    main()