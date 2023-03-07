test_tup = (15, 20, 123, 47, 26, 81)

sum = 0

loop_index = 0
while loop_index < len(test_tup):
    sum += test_tup[loop_index]
    loop_index += 1

print(f"Sum: {sum}")