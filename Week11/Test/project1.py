class Employee:
    def __init__(self, name, empNum):
        self.__name = name
        self.__empNum = empNum
    
    def set_name(self, name):
        self.__name = name
    def set_empNum(self, empNum):
        self.__empNum = empNum

    def get_name(self):
        return self.__name
    def get_empNum(self):
        return self.__empNum
    
    def __str__(self):
        return f'Name: {self.__name}\nEmployee Number: {self.__empNum}\n'

class ProductionWorker(Employee):
    def __init__(self, name, empNum, shift, hourlyPay):
        super().__init__(name, empNum)
        self.__shift = int(shift)
        self.__hourlyPay = hourlyPay

    def set_shift(self, shift):
        self.__shift = shift
    def set_hourlyPay(self, hourlyPay):
        self.__hourlyPay = hourlyPay

    def get_shift(self):
        if self.__shift == 1:
            return 'Day'
        elif self.__shift == 2:
            return 'Night'
        elif self.__shift == 3:
            return 'Day and Night'
        else:
            return 'Unknown'
    def get_hourlyPay(self):
        return self.__hourlyPay
    
    def __str__(self):
        return f'Name: {super().get_name()}\nEmployee Number: {super().get_empNum()}\nShift: {self.get_shift()}\nHourly Pay: ${self.get_hourlyPay()}\n'

def traverseList(list):
    for item in list:
        print(item)

def main():
    worker1 = ProductionWorker('Kevin Munoz', '123', 1, 32.42)
    worker2 = ProductionWorker('Lucy Lu', '456', 2, 22.19)
    worker3 = ProductionWorker('James Corden', '789', 3, 27.94)

    workers = [worker1, worker2, worker3]
    traverseList(workers)

main()
