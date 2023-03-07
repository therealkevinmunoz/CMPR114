tests_needed = 5
test_total = 0

for test in range(1, tests_needed + 1):
    score = int(input(f"Enter your test score #{test}: "))
    test_total += score

average = test_total / tests_needed
print(f"Your average: {average}")

