# #An animal with Strings (immutable) for first and last name.
class Animal(object):
   
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name) 
    
    def change_name(self, new_first, new_last):
        self.first_name = new_first
        self.last_name = new_last
    

a = Animal("Alan", "Archaengal")
b= Animal ("Barney", "Bobo")
print "a.full_name():", a.full_name()
print "b.full_name():", b.full_name()

a.change_name("Archy", "Antelope")
print "a.full_name():", a.full_name()
print "b.full_name():", b.full_name()


# # A cupboard with a list (mutable) of contents
class Cupboard(object):
    def __init__(self, contents=None):
        if contents is None:
            contents = []
        self.contents = contents
    
    def add_to_cupboard(self, item):
        self.contents.append(item)
        
    def get_contents(self):
        return self.contents

c = Cupboard()
d= Cupboard()

c.add_to_cupboard("fruit")
d.add_to_cupboard("sugar")

print c.get_contents()
print d.get_contents()

e = Cupboard(["onions", "raisins"])
e.add_to_cupboard("radishes")
print e.get_contents()
