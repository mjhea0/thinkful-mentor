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

    def output_species(self):
        # Mike is a mammal.
        return "{} is a {}.".format(self.name, self.species)


# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance method
# print mikey.description()
# print mikey.speak("Gruff Gruff")
print mikey.output_species()
