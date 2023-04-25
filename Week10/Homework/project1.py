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


class ShiftSupervisor(Employee):
    def __init__(self, name, empNum, salary, bonus):
        super().__init__(name, empNum)
        self.__salary = salary
        self.__bonus = bonus
    
    def set_salary(self, salary):
        self.__salary = salary
    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus

    def __str__(self):
        return f'Name: {super().get_name()}\nEmployee Number: {super().get_empNum()}\nSalary: ${self.__salary}\nBonus: ${self.__bonus}\n'

supervisor = ShiftSupervisor('Kevin Munoz', 1234, 55000, 5000)
supervisor2 = ShiftSupervisor('Fiona Buckley', 5678, 75000, 0)

print(supervisor)
print(supervisor2)
