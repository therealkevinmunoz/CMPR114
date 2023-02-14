month = int(input("Enter the month "));

if(month < 1 or month > 12):
    print("Enter a valid month");
elif (month >= 1 and month <= 3):
    print("Your month is in the first quarter");
elif (month >= 4 and month <= 6):
    print("Your month is in the second quarter");
elif (month >= 7 and month <= 9):
    print("Your month is in the third quarter");
elif (month >= 10 and month <= 12):
    print("Your month is in the fourth quarter");
