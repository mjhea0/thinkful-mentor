import sys

# get value
if sys.argv[1:]:
    upper_limit = sys.argv[1]
else:
    upper_limit = raw_input("Enter the upper limit of the range: ")

# convert to int / handle exceptions
while True:
    try:
        value = int(upper_limit)
        break
    except ValueError:
        upper_limit = raw_input(
            "Incorect data type. Please enter an 'integer' for the upper limit of the range: "
        )

# run fizzbuzz
for i in xrange(1, value + 1):
    if i % 15 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print i
