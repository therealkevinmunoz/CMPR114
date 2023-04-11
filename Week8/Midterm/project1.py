def collect_input():
    fat = float(input("Enter total grams of fat consummed today: "))
    carbs = float(input("Enter total grams of carbs consummed today: "))
    print(f"Today's Nutrition\nCalories from Fat: {calculate_fat(fat)}\nCalories from Carbohydrates: {calculate_carbs(carbs)}")


def calculate_fat(value):
    return value * 9

def calculate_carbs(value):
    return value * 4

collect_input()