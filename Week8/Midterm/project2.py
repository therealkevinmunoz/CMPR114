def readFile():
    inputFile = open('./Week8/Midterm/Coffee.txt', 'r')

    line_index = 0
    print('Description | Product Number | Price')
    for line in inputFile:
        line_content = line.split(',')
        if line_index != 0:
            print(f'{line_content[0]} - {line_content[1]} \n\t${line_content[2]}')
        line_index += 1
    inputFile.close()


def is_new_input():
    try:
        selection = input('Would you like to add a new coffee entry? (y = yes, n = no) ')
        if selection == 'y':
            return True
        elif selection == 'n':
            return False
    except:
        print("Invalid input. Try again")
        is_new_input()

def add_product():
    outputFile = open('./Week8/Midterm/Coffee.txt', 'a')
    coffee_name = input("Enter coffee name: ")
    product_number = input("Enter product number: ")
    price = input("Enter price ")

    outputFile.write(f'\n{coffee_name},{product_number},{price}')
    print('Added!')
    outputFile.close()



readFile()
if is_new_input():
    add_product()
    readFile()