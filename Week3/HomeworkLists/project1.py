def get_scores():
    test_scores = [];
    again = 'y';

    while again == 'y':
        value = float(input('Enter a test score: '))
        test_scores.append(value)

        print('Do you want to add another test score?')
        again = input('y = yes, anything else = no: ')
        print()

    return test_scores

def get_total(test_scores):
    total = 0.0
    for num in test_scores:
        total += num
    return total


print(f'Your total score: {get_total(get_scores())}')