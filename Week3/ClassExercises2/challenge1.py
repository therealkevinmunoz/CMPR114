MAX = 5;
SUM = 0

for counter in range(MAX):
    number = float(input('Enter a number: '));
    SUM += number;

print('Average: ' + str(SUM/5));