def write():
    outFile = open('Week6/Homework/things.txt', 'w')
    #collect user data
    animal = input("Enter an animal: ")
    fruit = input("Enter a fruit: ")
    country = input("Enter a country: ")

    outFile.write(f'Animal: {animal}\nFruit: {fruit}\nCountry: {country}')

    outFile.close()

write()
#read the file with user information
def read():
    inFile = open('Week6/Homework/things.txt', 'r')

    for line in inFile:
        print(line)

    inFile.close()

read()
