import sys

if sys.argv[1:]:
    upper_limit = sys.argv[1]
else:
    upper_limit = raw_input("Enter the upper limit of the range: ")

for i in xrange(1, int(upper_limit)+1):
    if i % 15 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print i

    