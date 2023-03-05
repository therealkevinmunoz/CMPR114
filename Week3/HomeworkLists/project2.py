def get_numbers():
    numbers_list = []
    numbers_needed = 20

    for count in range(numbers_needed):
        current_number = int(input('Enter a number: '))
        numbers_list.append(current_number)
    return numbers_list

def highest_number(value_list):
    highest_number = 0
    initialized = False
    for value in value_list:
        if value > highest_number or initialized == False:
            initialized = True
            highest_number = value
    return highest_number

def lowest_number(value_list):
    lowest_number = 0
    initialized = False
    for value in value_list:
        if value < lowest_number or initialized == False:
            initialized = True
            lowest_number = value
    return lowest_number

def total(value_list):
    total = 0
    for value in value_list:
        total += value
    return total

def average(value_list):
    total = 0
    total_values = len(value_list)
    for value in value_list:
        total += value

    average = total/total_values
    return average

number_list = get_numbers()

print(f'Highest Number Entered: {highest_number(number_list)}')
print(f'Lowest Number Entered: {lowest_number(number_list)}')
print(f'Total of Numbers Entered: {total(number_list)}')
print(f'Average of Numbers Entered: {average(number_list)}')