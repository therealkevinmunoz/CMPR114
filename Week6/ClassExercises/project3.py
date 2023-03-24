def sales():
    outFile = open("Week6/ClassExercises/sales.txt", "w")

    num_days = int(input("Enter number of days of sales: "))
    #repeat sales collection for days inputted
    for day in range(1, num_days +1):
        sales_amount = float(input(f"Enter sales for day {day}: "))
        outFile.write(f"{sales_amount}\n")

    outFile.close()
    print('Sales recorded')

sales()

#collect salary to add comission
def AddCommission():
    salary = float(input("Entern your salary: "))
    return salary

def WriteSalary(salary):
    outFile = open("Week6/ClassExercises/sales.txt", "a")
    outFile.write(f"{salary:.2f}")
    outFile.close()

def ReadSales():
    sales_file = open("Week6/ClassExercises/sales.txt", "r")
    line = sales_file.readline()
    total_amount = 0

    while line != "":
        amount = float(line)
        total_amount += amount
        print(f"{amount:.2f}")
        line = sales_file.readline()

    salary = AddCommission()

    #give bonus if the sales is greater than 1000
    if(total_amount > 1000):
        salary = salary * 1.10
    
    WriteSalary(salary)

    sales_file.close()

ReadSales()

