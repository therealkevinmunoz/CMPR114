product = 0;

while product < 100:
    number = float(input('Enter a number: '));
    product += number * 10;
    print('Product: ' + str(product));