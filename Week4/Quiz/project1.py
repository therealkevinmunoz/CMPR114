salary = float(input("Enter your salary: "))

gross_salary = salary * 1.10

formatted_salary = "{:,.2f}".format(gross_salary)

print(f"${formatted_salary}")