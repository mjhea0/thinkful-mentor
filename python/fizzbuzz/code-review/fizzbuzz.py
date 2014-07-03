__author__ = 'hpiard'
import sys

print "This is my fizzbuzz program."

# Requirements:
# If user supplies value at command line when script runs, we'll use that value.
# Otherwise, we'll use the raw_input() dialogue to get an input from the user.

if sys.argv[1:]:
    userinput = sys.argv[1]
else:
    userinput = raw_input("Enter the upper limit of the range: ")

# use format() function rather than string interpolation
# http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format
print "Fizzbuzz counting up to {0}".format(userinput)

# no real need to asign these to variables
fizzbuzz = "fizz buzz"
fizz = "fizz"
buzz = "buzz"

# use xrange rather than range for python 2.7x
for i in xrange(1, int(userinput) + 1):
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
