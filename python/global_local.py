""" Demonstrating hoisting a variable to the enclosing
scope using "global"""

foo = 1

def f():
    b = foo + 1
    print b

f()


def g():
    global barney  #hoist this to the enclosing scope (dont do this.)
    barney = "locally defined"
    print "hello"

g()
print barney
