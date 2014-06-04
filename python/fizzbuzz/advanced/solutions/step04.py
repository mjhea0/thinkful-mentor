def fizzbuzz(upper_limit):
    output_list = []
    for num in xrange(1, upper_limit+1):
        if num % 15 == 0:
            output_list.append("FizzBuzz")
        elif num % 3 == 0:
            output_list.append("Fizz")
        elif num % 5 == 0:
            output_list.append("Buzz")
        else:
            output_list.append(num)
    return output_list

if __name__ == '__main__':
    output = fizzbuzz(30)
    for num in output:
        print num


"""
Can you think of any benefits of assigning
the function to the variable output?
"""
