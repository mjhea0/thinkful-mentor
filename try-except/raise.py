# Custom exceptions:
# http://infohost.nmt.edu/tcc/help/pubs/python/web/raise-statement.html
# http://pydanny.com/attaching-custom-exceptions-to-functions-and-classes.html


import sys

def raise_test(filename):
    try:
        f = open(filename)
        s = f.readline()
        i = int(s.strip())
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    except ValueError:
        print "No valid integer in line."
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

### --- run code --- ###

raise_test('integers.txt')
raise_test('ints.txt')
