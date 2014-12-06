# #super


class Animal(object):
    def __init__(self, name=None):
        self.name = name


class Dog(Animal):
    def __init__(self, name=None, housebroken=False):
        super(Dog, self).__init__(name)
        self.housebroken = housebroken
        


class Cat(Animal):
    def __init__(self, name=None, declawed=False):
        super(Cat, self).__init__(name)
        self.declawed = declawed
        


fido = Dog("fido", True)
fluffy = Cat("fluffy", False)


print vars(fido)


print vars(fluffy)


spot = Dog("spot")


print vars(spot)


hershey = Dog("hershey", housebroken=True)

print vars(hershey)


