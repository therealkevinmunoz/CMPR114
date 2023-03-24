def main():
    num_emps = int(input("Enter the number of employee records "))
    emp_file = open("Week6/ClassExercises/employee.txt", "w")

    #collect employee info for each employee specified
    for count in range(1, num_emps +1):
        print(f"Enter data for employee {count}")
        name = input("Name: ")
        id_num = input("ID Number: ")
        dept = input("Department: ")

        emp_file.write(f"{name}\n")
        emp_file.write(f"{id_num}\n")
        emp_file.write(f"{dept}\n")
        
        print()

    emp_file.close()
    print('Recorded')

main()

def ReadEmployee():
    emp_file = open("Week6/ClassExercises/employee.txt", "r")

    for line in emp_file:
        print(line)

    emp_file.close

ReadEmployee()