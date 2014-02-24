# Custom exceptions:
# http://infohost.nmt.edu/tcc/help/pubs/python/web/raise-statement.html
# http://pydanny.com/attaching-custom-exceptions-to-functions-and-classes.html


import sys

def raise_test(filename):
    try:
        f = open(filename)
        s = f.readline()
        i = int(s.strip())
    except (IOError, ValueError) as e:
        print "oops"

### --- run code --- ###

raise_test('integers2.txt')
raise_test('ints.txt')
