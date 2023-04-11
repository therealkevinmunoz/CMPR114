number_list = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def get_sum(array):
    sum = 0
    for value in array:
        sum += value
    return sum

def get_average(sum, total):
    average = sum / total
    return average

sum = get_sum(number_list)
print(f"Sum: {sum}\nAverage: {get_average(sum, len(number_list))}")
