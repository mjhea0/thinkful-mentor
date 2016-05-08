class Parrot:

    def __init__(self, name="Happy"):
        self.name = name

    def talk(self):
        message = '{0} wants a cracker!'.format(self.name)
        print(message)

polly = Parrot()
polly.name = "Polly"
polly.talk()

jimmy = Parrot()
jimmy.talk()
