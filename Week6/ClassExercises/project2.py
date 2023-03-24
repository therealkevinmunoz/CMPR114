def WriteNumbers():
    outfile = open('Week6/ClassExercises/numbers.txt', 'w')
    num1 = int(input("1. Enter a number: "))
    num2 = int(input("2. Enter a number: "))
    num3 = int(input("13 Enter a number: "))

    sum = num1 + num2 + num3
    avg = sum/3
    #write each number to the output file
    outfile.write(f"The 1st number is {num1}\n")
    outfile.write(f"The 2nd number is {num2}\n")
    outfile.write(f"The 3rd number is {num3}\n")
    outfile.write(f"The total number is {sum}\n")
    outfile.write(f"The average is {avg}\n")

    print('Data recorded')

    outfile.close()

    return outfile

WriteNumbers()

def ReadNumbers():
    inFile = open("Week6/ClassExercises/numbers.txt", 'r')
    for line in inFile:
        print(line)

ReadNumbers()