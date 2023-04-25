class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_telephone(self, telephone):
        self.__telephone = telephone

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_telephone(self):
        return self.__telephone
    
    def __str__(self):
        return f'Name: {self.__name}\nAddress: {self.__address}\nTelephone: {self.__telephone}'

class Customer(Person):
    def __init__(self, name, address, telephone, customerNumber, isSubscribed):
        super().__init__(name, address, telephone)
        self.__customerNumber = customerNumber
        self.__isSubscribed = isSubscribed
    
    def set_customerNumber(self, customerNumber):
        self.__customerNumber = customerNumber
    def set_isSubscribed(self, isSubscribed):
        self.__isSubscribed = isSubscribed

    def get_customerNumber(self):
        return self.__customerNumber
    def get_isSubscribed(self):
        if self.__isSubscribed:
            return 'Subscribed'
        else:
            return 'Unsubscribed'

    def __str__(self):
        return f'Name: {super().get_name()}\nAddress: {super().get_address()}\nTelephone: {super().get_telephone()}\nCustomer Number: {self.get_customerNumber()}\nMailing List Status: {self.get_isSubscribed()}\n'
    
customer = Customer('Jim Parsons', '1201 N Mountain View', 7141345673, 123, True)
customer1 = Customer('Olivia Wiley', '3408 Grand Ave', 714234543, 345, False)

print(customer)
print(customer1)

    