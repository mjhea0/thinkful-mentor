import sys


def get_value():
    if sys.argv[1:]:
        upper_limit = sys.argv[1]
    else:
        upper_limit = raw_input("Enter the upper limit of the range: ")
    return upper_limit


def convert_value(upper_limit):
    while True:
        try:
            value = int(upper_limit)
            return value
        except ValueError:
            upper_limit = raw_input(
                "Incorect data type. Please enter an 'integer' for the upper limit of the range: "
            )


def fizzbuzzed(upper_limit=30):
    for i in xrange(1, upper_limit+1):
        if is_divisible(i, 15):
            print "FizzBuzz"
        elif is_divisible(i, 5):
            print "Fizz"
        elif is_divisible(i, 3):
            print "Buzz"
        else:
            print i


def is_divisible(num1, num2):
    return num1 % num2 == 0


if __name__ == '__main__':
    value = get_value()
    converted_value = convert_value(value)
    fizzbuzzed(converted_value)
