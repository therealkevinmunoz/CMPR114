class RetailItem:
    def __init__(self, desc, units, price):
        self.__desc = desc
        self.__units = units
        self.__price = price
    
    def set_desc(self, desc):
        self.__desc = desc
    def set_units(self, units):
        self.__units = units
    def set_price(self, price):
        self.__price = price

    def get_desc(self):
        return self.__desc
    def get_units(self):
        return self.__units
    def get_price(self):
        return self.__price
    
    def __str__(self):
        return f'Item Description: {self.__desc}\nUnits in Inventory: {self.__units}\nPrice: ${self.__price}\n'

RetailItem1 = RetailItem('Jacket', 12, 59.95)
RetailItem2 = RetailItem('Designer Jeans', 40, 34.95)
RetailItem3 = RetailItem('Shirt', 20, 24.95)

print(str(RetailItem1))
print(str(RetailItem2))
print(str(RetailItem3))