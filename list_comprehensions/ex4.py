# dict comps - ex4


num_list = [2, 4, 6]
keys = [1, 3, 5]

print dict((x, y) for x in keys for y in num_list)
print dict(zip(keys, num_list))


class Person(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "{} ({})".format(self.name, self.id)

people = [
    Person(1, 'Josh'),
    Person(2, 'Megan'),
    Person(3, 'Ken')
]

print dict([(p.id, p) for p in people])