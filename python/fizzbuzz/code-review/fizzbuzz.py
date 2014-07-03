__author__ = 'hpiard'
import sys

print "This is my fizzbuzz program."
userinput = int(sys.argv[1])

# use format() function rather than string interpolation
# http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format
print "Fizzbuzz counting up to {0}".format(userinput)

# no real need to asign these to variables
fizzbuzz = "fizz buzz"
fizz = "fizz"
buzz = "buzz"

for i in range(1, userinput + 1):
    # if (i % 3 == 0) and (i % 5 == 0):
    # slightly simplier syntax
    if (i % 15 == 0):
        print "FizzBuzz"
    elif (i % 3 == 0) and (i % 5 != 0):
        print "Fizz"
    elif (i % 3 != 0) and (i % 5 == 0):
        print "Buzz"
    else:
        print i
