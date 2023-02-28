def total(): 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    sum = 0;

    file = open('Week3/ClassListExercises3/challenge1.txt', 'w');

    for value in numbers:
        file.write(str(value) + '\n');
        sum += value;
    
    average = sum/len(numbers);
    print(f'The average is {average}. The sum is {sum}');

    file.write(f'The average is {average}. The sum is {sum}');
    print('File challenge1.txt has been created')

total();