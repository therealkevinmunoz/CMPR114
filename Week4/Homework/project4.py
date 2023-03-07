def sort_sum(tupple):
    sum_list = []

    for nest1_item in tupple:
        current_sum = 0

        for nest2_item in nest1_item:
            current_sum += nest2_item
        sum_list.append(current_sum)       
        

    sum_list.sort()
    return sum_list

input_tup = ([2, 20], [44, 1], [3, 13])

print(sort_sum(input_tup))