average = 0

while average > 100 or average == 0:

    if average > 100:
        print("You will need to reenter 4 scores")
        
    scores_needed = 4
    total_score = 0
    score_list = []

    for score in range(1, scores_needed + 1):
        current_score = float(input(f"Enter test score #{score}: "))
        total_score += current_score
        score_list.append(current_score)

    for test_score in score_list:
        if test_score >= 90 and test_score < 100:
            print(f"A: {test_score}")
        elif test_score >= 80 and test_score < 89:
            print(f"B: {test_score}")
        elif test_score >= 70 and test_score < 79:
            print(f"C: {test_score}")
        elif test_score >= 60 and test_score < 69:
            print(f"D: {test_score}")
        elif test_score < 60:
            print(f"F: {test_score}")

    average = total_score/scores_needed
    print(f"Your average: {average}")

