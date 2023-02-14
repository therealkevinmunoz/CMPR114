quantity = int(input("How many software packages did you buy "));

discount = 1;
pre_discount_price =  99 * quantity;
total_price = 0;


if(quantity >= 10 or quantity <= 19):
    discount = .90
    total_price = pre_discount_price * discount
    print("Your price is $", total_price);
elif(quantity >= 20 or quantity <= 49):
    discount = .80
    total_price = pre_discount_price* discount
    print("Your price is $", total_price);
elif (quantity >= 50 and quantity <= 99):
    discount = .70
    total_price = pre_discount_price * discount
    print("Your price is $", total_price);
elif (quantity >= 100):
    discount = .60
    total_price = pre_discount_price * discount
    print("Your price is $", total_price);
else:
    total_price = pre_discount_price
    print("Your price is $", total_price);