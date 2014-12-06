# define a function to use as a filter.  Here we are filtering out 
#evens
def f(x): return x%2 != 0
print filter(f, range(0,20))


# or use a lambda
# here we are keeping only evens.
print filter(lambda x: x % 2 == 0, range(0,20))


# a more complicated example
wines = [
    { 
        'color':'red',
        'age':23,
        'mfg': 'Calabrese'
    },
    {
        'color':'white',
        'age':5,
        'mfg':'Napa'
    },
    {
        'color':'red',
        'age':10,
        'mfg':'Nerito'
    }
]

# show me only red wines
print filter(lambda x: x['color'] == 'red', wines)

# show me the manufacturers of those wines
mfgs = [wine["mfg"] for wine in filter(lambda x: x['color'] == 'red', wines)]
print "red wine manufacturers: ", mfgs