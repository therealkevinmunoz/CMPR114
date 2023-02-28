inputs_collected = False; 
total_inputs = 0;
sum = 0;

while total_inputs < 4:
    input_numeral = float(input('Enter a sales comission '))
    total_inputs += 1;
    sum += input_numeral;


print('Total Sales Commission: ' + str(sum));