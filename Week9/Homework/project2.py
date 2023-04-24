class Employee:
    def __init__(self, name, idnumber, dept, title):
        self.__name = name
        self.__idnumber = idnumber
        self.__dept = dept
        self.__title = title
    
    def set_name(self, name):
        self.__name = name
    def set_idnumber(self, idnumber):
        self.__idnumber = idnumber
    def set_dept(self, dept):
        self.__dept = dept
    def set_title(self, title):
        self.__title = title

    def get_name(self):
        return self.__name
    def get_idnumber(self):
        return self.__idnumber
    def get_dept(self):
        return self.__dept
    def get_title(self):
        return self.__title
    
    def __str__(self):
        return f'Name: {self.__name}\nID Number: {self.__idnumber}\nDepartment: {self.__dept}\nTitle: {self.__title}'

Employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
Employee2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
Employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

print(str(Employee1) + '\n')
print(str(Employee2) + '\n')
print(str(Employee3))