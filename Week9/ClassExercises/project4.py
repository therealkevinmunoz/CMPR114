class Customer:
    def __init__(self, name, address, phone, city, zip, age):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__city = city
        self.__zip = zip
        self.__age = age
    
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone
    def set_city(self, city):
        self.__city = city
    def set_zip(self, zip):
        self.__zip = zip
    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone
    def get_city(self):
        return self.__city
    def get_zip(self):
        return self.__zip
    def get_age(self):
        return self.__age

def main():
    name = input('Enter your name: ')
    address = input('Enter your address: ')
    phone = input('Enter your phone: ')
    city = input('Enter your city: ')
    zip = input('Enter your zip code: ')
    age = input('Enter your age: ')

    Customer1 = Customer(name, address, phone, city, zip, age)
    v1 = Customer1.get_name()
    v2 = Customer1.get_address()
    v3 = Customer1.get_phone()
    v4 = Customer1.get_city()
    v5 = Customer1.get_zip()
    v6 = Customer1.get_age()

    print('Hi ' + v1 + ' your address is ' + v2 + ' ' + v4 + ', ' + v5 + '. Your phone # is ' + v3 + '. Your age is ' + v6)

main()