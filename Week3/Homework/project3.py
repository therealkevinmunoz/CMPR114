SUM = 0
initial_number = float(input("Enter a postive number to add sum (or negative number to end) "))

while  initial_number >= 0:
    SUM += initial_number
    initial_number = float(input("Enter a postive number to add sum (or negative number to end) "))

print(f"Your Sum: {SUM}")