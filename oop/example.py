class Add(object):

    def __init__(self, number):
        self.number = number

    def add_one(self):
        return (self.number + 1)



if __name__ == '__main__':
    create = Add(10)
    print create.add_one()
