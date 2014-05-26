class Dog(object):

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
    def moves(self, verb):
        return "{} is {}".format(self.name,verb)

# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance method
print mikey.description()
print mikey.speak("Gruff Gruff")

andrew = Dog("Andrew",15)
print andrew.moves("walking")
