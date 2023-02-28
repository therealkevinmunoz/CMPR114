RAINFALL = []
MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
TOTAL_MONTHS = 12

total_rainfall = 0;
average_rainfall = 0;
lowest_rainfall = 0;
highest_rainfall = 0;

file = open('challenge3rainfall.txt', 'w');

for month in range(TOTAL_MONTHS):
    monthly_rainfall = float(input(f'Enter the rainfall for {MONTH[month]} '));
    RAINFALL.append(monthly_rainfall);

month_index = 0

for rainfall in RAINFALL:
    file.write(f'{MONTH[month_index]}: {rainfall} inches\n')
    total_rainfall += rainfall;
    month_index += 1;

    if rainfall < lowest_rainfall or lowest_rainfall == 0:
        lowest_rainfall = rainfall; 

    if rainfall > highest_rainfall:
       highest_rainfall = rainfall; 


file.write(f'Your total rainfall is {total_rainfall} inches\n');
print(f'Your total rainfall is {total_rainfall} inches\n');

average_rainfall = total_rainfall/12;
file.write(f'Your average rainfall is {average_rainfall} inches\n');
print(f'Your average rainfall is {average_rainfall} inches\n');

file.write(f'Your highest rainfall is {highest_rainfall} inches\n');
print(f'Your highest rainfall is {highest_rainfall} inches\n');

file.write(f'Your lowest rainfall is {lowest_rainfall} inches\n');
print(f'Your lowest rainfall is {lowest_rainfall} inches\n');

print('Your file challenge3rainfall.txt has been created.');
