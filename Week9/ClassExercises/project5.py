import bankaccount

def main():
    start_bal = float(input('Enter your starting balance: '))
    savings = bankaccount.BankAccount(start_bal)

    pay = float(input('How much were you paid this week: '))
    print(f'${pay} will be deposited into your account')
    savings.depost(pay)
    print(f'Your balance: ${savings.get_balance():.2f}')

    cash = float(input('How much would you like to withdraw: '))
    print(f'${cash} will be withdrawn from your account')
    savings.withdraw(cash)
    print(f'Your balance: ${savings.get_balance():.2f}')


main()