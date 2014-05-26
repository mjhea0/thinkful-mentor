class FizzBuzz(object):

    def fizzbuzz(self, num):
        if not(num % 5) and not(num % 3):
            return "fizzbuzz"
        elif not(num % 3):
            return "fizz"
        elif not(num % 5):
            return "buzz"
        else:
            return num

test = FizzBuzz()
result = test.fizzbuzz(25)
print result
