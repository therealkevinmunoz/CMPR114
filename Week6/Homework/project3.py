def write():
    outFile = open('Week6/Homework/number_list.txt', 'w')
    #collect user data
    for number in range(1,101):
     outFile.write(str(number) + "\n")

    print (f"The file Week6/Homework/number_list.txt was created")
    outFile.close()

write()
