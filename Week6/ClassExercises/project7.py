def collect_student_info():
    try:
        name = input("Enter your full name: ")
        midterm_score = float(input("Enter your midterm grade: "))
        final_score = float(input("Enter your final exam grade: "))
        avg_score = get_average(midterm_score, final_score)
        letter_grade = get_letter_grade(avg_score)
        #write to file
        write([name, "Average: " + str(avg_score), "Grade: " + letter_grade])
        read()
    except ValueError:
        print("Enter a valid value. Try again.")
        collect_student_info()
    except:
        print("An issue occured. Try again")
        collect_student_info()

#function to find the average
def get_average(score1, score2):
    avg = (score1 + score2)/2
    return avg

#function to find the letter grade
def get_letter_grade(score):
    if score > 90 and score <= 100:
        return "A"
    elif score > 80 and score < 90:
        return "B"
    elif score > 70 and score < 80:
        return "C"
    elif score > 60 and score < 70:
        return "D"
    elif score >= 0 and score < 60:
        return "F"
    
def write(array):
    grade_file = open("Week6/ClassExercises/gradeReport.txt", "w")
    for value in array:
        grade_file.write(value + "\n")

def read():
    grade_file = open("Week6/ClassExercises/gradeReport.txt", "r")
    for line in grade_file:
        print(line)

collect_student_info()