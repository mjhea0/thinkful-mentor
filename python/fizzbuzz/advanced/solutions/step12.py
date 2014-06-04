def get_value():
    upper_limit = raw_input("Enter the upper limit of the range: ")
    return upper_limit


def validate_number(upper_limit):
    while True:
        try:
            value = int(upper_limit)
            return value
        except ValueError:
            upper_limit = raw_input(
                "Incorect data type. Please enter an 'integer' for the upper limit of the range: "
            )


def fizzbuzz(upper_limit):
    output_list = []
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
    return num1 - (num1 // num2 * num2) == 0


if __name__ == '__main__':
    value = get_value()
    validated_value = validate_number(value)
    output = fizzbuzz(validated_value)
    for num in output:
        print num
