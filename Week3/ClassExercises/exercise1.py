inputs_collected = False; 
total_inputs = 0;
sum = 0;
average = 0;

while total_inputs < 4:
    input_numeral = float(input('Enter a temperature '))
    if(input_numeral > 102.5):
        print('Invalid numeral entered');
    else:
        total_inputs += 1;
        sum += input_numeral;

average = sum/4;
print('Average: ' + str(average));
print('Sum: ' + str(sum));