class Dog(object):

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return self.name, self.age

    # instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # class method
    def get_species(cls):
        return cls.species


# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our class method
print mikey.get_species()
