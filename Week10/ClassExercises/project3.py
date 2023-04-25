class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_mileage(self, mileage):
        self.__mileage = mileage
    def set_price(self, price):
        self.__price = price

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return f'Make: {self.__make}\nModel: {self.__model}\nMileage: {self.__mileage}\nPrice: ${self.__price}\n'

audi = Automobile('Audi', 2022, 45000, 80000.0)
honda = Automobile('Honda', 2022, 45000, 80000.0)
toyota = Automobile('Toyota', 2018, 75000, 40000.0)

print(audi)
print(honda)
print(toyota)
