# functions
def get_value():
    """As the user for a value."""
    upper_limit = raw_input("Enter the upper limit of the range: ")
    return upper_limit


def validate_number(upper_limit):
    """"
    Ensure that provided number is an integer.
    If not, enter a loop, asking user for an integer.
    Only exit loop when a integer is provided,
    """
    while True:
        # exception handling
        try:
            value = int(upper_limit)  # data types
            return value
        except ValueError:
            upper_limit = raw_input(
                "Incorect data type. Please enter an 'integer' for the upper limit of the range: "
            )


def fizzbuzz(upper_limit):
    """
        Classic fizzbuzz:
          Given a range -
          - For multiples of three print "Fizz" instead of the number
          - For the multiples of five print "Buzz"
          - For numbers which are multiples of both three and five print "FizzBuzz"
    """
    output_list = []  # data structures
    for num in xrange(1, upper_limit+1):
        if is_divisible(num, 15):
            output_list.append("FizzBuzz")
        elif is_divisible(num, 3):
            output_list.append("Fizz")
        elif is_divisible(num, 5):
            output_list.append("Buzz")
        else:
            output_list.append(num)
    return output_list


def is_divisible(num1, num2):
    """Return True if num1 is divisible by num2"""
    return num1 - (num1 // num2 * num2) == 0  # algorithms


if __name__ == '__main__':
    value = get_value()
    validated_value = validate_number(value)
    output = fizzbuzz(validated_value)
    for num in output:
        print num
