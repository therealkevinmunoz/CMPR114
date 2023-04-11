values = [[1, 2, 3], [10, 20, 30], [5, 6, 7]]
values2 = [[1, 2, 3], [10, 20, 30], [5, 6, 8]]

def get_lucky_number(array):
    lucky_number = 7
    lucky_number_found = False
    for numberlist in array:
        for number in numberlist:
            if number == lucky_number:
                lucky_number_found = True

    return lucky_number_found

def print_message(is_found):
    if is_found:
        print("Found number 7!")
    else:
        print("The lucky number was not in this list.")


print_message(get_lucky_number(values))
#print_message(get_lucky_number(values2))