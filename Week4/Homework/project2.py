test_tup = (15, 20, 123, 47, 26, 81)

def find_largest(list):
    largest_number = 0

    loop_index = 0
    while loop_index < len(test_tup):
        if loop_index == 0:
            largest_number = test_tup[loop_index]
        elif test_tup[loop_index] > largest_number:
            largest_number = test_tup[loop_index]

        loop_index += 1
    return largest_number

print(f"Largest number in Tuple: {find_largest(test_tup)}")
