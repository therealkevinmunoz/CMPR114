#read the file with user information
def read():
    inFile = open('Week6/Homework/things.txt', 'r')

    for line in inFile:
        print(line)

    inFile.close()

read()
