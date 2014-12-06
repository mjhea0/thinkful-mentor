def foo(a, b, c):
    print "a={}, b={}, c={}".format(a,b,c)


def bar(q="quail", b="barney"):
    print "q={}, b={}".format(q, b)

args = [1, 2, 3]

foo(*args)

d = {"q" : "yakitori" , "b" : "cosmic"}
bar(**d)
