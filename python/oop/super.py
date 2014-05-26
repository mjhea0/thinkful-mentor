class ParentClass(object):
    def __init__(self, a, b):
        print "a", a
        print "b", b

class ChildClass(ParentClass):
    def __init__(self, c, d, *args, **kwargs):
        print "c", c
        print "d", d
        super(ChildClass, self).__init__(*args, **kwargs)

test = ChildClass(1,2,3,4)

"""
The super(ChildClass, self).__init__(*args, **kwargs) instruction means "call the constructor of the parent class of 
ChildClass with arguments *args, **kwargs".

You have ParentClass that does some useful things. And you have to use this class everywhere in your applicatio 
with adding some piece of functionality. You may inherit this class ChildClass(ParentClass) and expand it's
functionality. Now you can use ChildClass instead of class ParentClass everywhere and get rid of redundant operation.

args example:

def test_var_args(foo, *args):
   pass

test_var_args(1, "two", 3)

keyword args example:

def test_var_kwards(foo, **kwargs):
  pass

test_var_kwargs(foo=1, myarg2="two", myarg3=3)
"""

