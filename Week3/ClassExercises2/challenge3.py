SUM = 0

for counter in range(1, 6):
    number = float(input('Enter number of bugs collected on Day ' + str(counter) + ': '));
    SUM += number;

print('Total Bugs: ' + str(SUM));