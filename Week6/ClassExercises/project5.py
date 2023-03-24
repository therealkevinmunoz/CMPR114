def main():
    while True:
        try:
            hours = int(input('Hours worked: '))
            pay = float(input('Hourly pay: '))
            gross = hours * pay
            print(f"Gross pay: ${gross:.2f}")
            print('recorded')
            break
        except ValueError:
            print("ERROR: Hours worked and hourly pay must be valid numbers, try again.")
        except Exception as err:
            print(err)

main()