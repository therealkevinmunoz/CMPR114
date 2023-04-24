class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    def set_name(self, name):
        self.__name = name
    def set_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age

def main():
    name = input('Enter your pet\'s name: ')
    animal_type = input('Enter the breed of your pet: ')
    age = input('Enter your age: ')

    Pet1 = Pet(name, animal_type, age)
    v1 = Pet1.get_name()
    v2 = Pet1.get_type()
    v3 = Pet1.get_age()

    print('Your Pet: ' + v1 + ' is a ' + v2 + ' and is ' + v3 + ' years old.')

main()