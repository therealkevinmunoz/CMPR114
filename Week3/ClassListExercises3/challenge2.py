SALES = []
DAY_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
TOTAL_DAYS = 7
total_sales = 0;
file = open('Week3/ClassListExercises3/challenge2sales.txt', 'w');

for day in range(TOTAL_DAYS):
    daily_sale = float(input(f'Enter the sales for {DAY_OF_WEEK[day]} '));
    SALES.append(daily_sale);

sale_index = 0
for sale in SALES:
    file.write(f'{DAY_OF_WEEK[sale_index]}: ${sale} \n')
    total_sales += sale;
    sale_index += 1;


file.write(f'Your total sales are ${total_sales}');
print(f'Your total sales are ${total_sales}');
print('Your file challenge2sales.txt has been created.');
