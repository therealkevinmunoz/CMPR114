class BankAccount:
    def __init__(self, bal):
        self.__balance = bal
    def depost(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Error: Insufficient funds.')
        else:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance