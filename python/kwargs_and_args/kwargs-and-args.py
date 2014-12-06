
# "Positional" arguments
def foo(alpha, beta, gamma):
    print alpha + beta + gamma

print "foo"
foo(1, 1, 1)
foo(*[2,2,2])
print 


# keyword argument with defaults.
def qux(alpha, beta, gamma=3):
    print alpha + beta + gamma

print "qux"
qux(beta=3, alpha=3) #notice also out of order.
print



def invalid(alpha, beta):
    print alpha + beta
#invalid(alpha=1, beta=2, gamma=3)



def bar(**kwargs):
    print kwargs["alpha"] + kwargs["beta"]

print "bar"
bar(alpha=25, beta=30)
print 





# Lets explore whats in kwargs.
def list_kwargs(**kwargs):
    for k,v in kwargs.iteritems():
        print "{}: {}".format(k, v)

print "list_kwargs"
list_kwargs(yoko="ono", john="lennon")
print





# variable list of unnamed args.  
def baz(*args):
    print args[0] + args[1]

print "baz"
baz(2, 3)
print







# some "positional" args plus kwargs.
def corge(alpha, beta, gamma, **kwargs):
    print alpha + beta + gamma + kwargs["delta"]

print "corge"
corge(10,10,10, delta=4)
print






