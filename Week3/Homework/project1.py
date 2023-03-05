speed = int(input("What was the speed of the vehicle in mph? "))
hours_traveled = int(input("How many hours has it traveled? "))

distance_traveled = 0

for hour in range(1, hours_traveled + 1):
    distance_traveled += speed
    print(f'Hour {hour}: {distance_traveled} miles')

