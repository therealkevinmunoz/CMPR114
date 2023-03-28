def main():
    names = ['Howard', 'Jamie', 'Jill']
    print("The list before we insert or remove")
    print(names)
    name_remove = input("Enter the name to remove: ")
    names.insert(0, 'Joe')
    names.remove(name_remove)
    print('The list after the insert and remove')
    print(names)

main()

def total():
    number_file = open("Week7/ClassExercises2/number_file.txt", "w")
    numbers = [1,2,3,4,5,6,7,8,9,10]
    sum = 0

    for value in numbers:
        number_file.write(str(value) + '\n')
        sum += value
    number_file.close()
    average = sum/len(numbers)
    print(f'The total is {sum}. The average is {average}')

total()