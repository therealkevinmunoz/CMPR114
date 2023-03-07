first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))


if age < 0:
    print("Invalid age")
else:
    print(f"{first_name} {last_name}, {age}")