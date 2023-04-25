class AnimalType:
    def eats(self):
        print('What does this animal like to eat? ')

class rabbit(AnimalType):
    def munch(self):
        print(' carrots ')

class bird(AnimalType):
    def munch1(self):
        print(' seeds ')

class monkey(AnimalType):
    def munch2(self):
        print(' banana ')

RabbitObject = rabbit()
RabbitObject.eats()
RabbitObject.munch()

BirdObject = bird()
BirdObject.eats()
BirdObject.munch1()

MonkeyObject = monkey()
MonkeyObject.eats()
MonkeyObject.munch2()
