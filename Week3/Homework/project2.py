years = int(input("Enter the number of years to average rainfall data: "))
total_rainfall = 0
MONTHS_IN_YEAR = 12
MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
total_months_collected = 0

for year in range(1, years + 1):
    print(f"Year {year}\n")

    for month in range(MONTHS_IN_YEAR):
        total_months_collected += 1
        this_month_rainfall = int(input(f"Enter rainfall for {MONTH[month]}: "))
        print(f"\t{MONTH[month]}: {this_month_rainfall} inches of rain\n")
        total_rainfall += this_month_rainfall
        

print(f"Data collected across {total_months_collected} months\n")
print(f"Total Rainfall: {total_rainfall} inches\n")
print(f"Average Rainfall: {total_rainfall/total_months_collected} inches\n")
