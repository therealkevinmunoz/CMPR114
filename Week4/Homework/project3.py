def find_sum(tupple):
    sum = 0
    for nest1_item in tupple:
        for nest2_item in nest1_item:
            sum += nest2_item
    return sum

test_tup = ([17, 28], [93, 11], [20, 17])

print(f"Sum: {find_sum(test_tup)}")