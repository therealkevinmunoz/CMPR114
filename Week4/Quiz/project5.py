sales = float(input("Enter your total sales: "))

if sales < 50000.00:
    print("You did not earn commission.")
elif sales >= 50000.00 and sales < 60000.00:
    salary = 70000.00
    print(f"Your commission: ${salary * 1.10}")
elif sales >= 60000.00 and sales < 80000.00:
    salary = 80000.00
    print(f"Your commission: ${salary * 1.20}")
elif sales >= 80000.00:
    salary = 90000.00
    print(f"Your commission: ${salary * 1.30}")