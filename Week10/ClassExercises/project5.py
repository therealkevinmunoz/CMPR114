class Insect:
    def __init__(self, name, wings):
        self.__name = name
        self.__wings = wings
    
    def set_name(self, name):
        self.__name = name
    def set_wings(self, wings):
        self.__wings = wings

    def get_name(self):
        return self.__name
    def get_wings(self):
        return self.__wings
    
    def __str__(self):
        return f'Name: {self.__name}\nWings: {self.__wings}\n'

class Bumblebee(Insect):
    def __init__(self, name, wings):
        super().__init__(name, wings)
    
    def sting(self):
        print(f'{super().get_name()} can sting you\n')

class Grasshopper(Insect):
    def __init__(self, name, wings):
        super().__init__(name, wings)
    
    def jump(self):
        print(f'{super().get_name()} is ready to jump\n')

bee = Bumblebee('Mr. Bee', 2)
grasshopper = Grasshopper('Mr. Hopper', 2)

print(bee)
bee.sting()
print(grasshopper)
grasshopper.jump()
