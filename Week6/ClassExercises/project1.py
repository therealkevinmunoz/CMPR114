def write():
    outFile = open('Week6/ClassExercises/myFile.txt', 'w')
    #collect user data
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))

    outFile.write(f'{first_name} {last_name} {age}')

    outFile.close()

write()
#read the file with user information
def read():
    inFile = open('Week6/ClassExercises/myFile.txt', 'r')

    fileContents = inFile.read()

    inFile.close()

    print(fileContents)

read()
