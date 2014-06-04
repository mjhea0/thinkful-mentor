def fizzbuzz(upper_limit):
    for num in xrange(1, upper_limit):
        if num % 15 == 0:
            print "FizzBuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num

if __name__ == '__main__':
    fizzbuzz(30)
