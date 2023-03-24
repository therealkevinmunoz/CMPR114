import random

def get_randomInt():
    randomInt_file = open("Week6/ClassExercises/randomInt.txt", "w")

    for index in range(0,10):
            randomInt = random.randint(1, 10)
            write(randomInt_file, randomInt)
    
    randomInt_file.close()

    read("Week6/ClassExercises/randomInt.txt")

    print("The file randomInt.txt has been created.")
    
    
def write(file, int):
    file.write(str(int) + "\n")

def read(filePath):
    randInt_file = open(filePath, "r")
    print("Reading contents of " + filePath)
    for line in randInt_file:
        print(line)
    randInt_file.close()

get_randomInt()