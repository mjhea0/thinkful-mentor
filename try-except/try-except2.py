# try/except example

def assert_positive(num_list):
    """assert that each number is greater than 0"""
    for num in num_list:
        try:
            assert num > 0
        except AssertionError:
            print "Sorry. " + str(num) + " is less than zero. Try again"
            return 0
        else:
            return 1


def calculate_total(num1,num2,num3):
    """calculate total from three numbers"""
    num_list = []
    num_list.extend((num1, num2, num3))
    if assert_positive(num_list) == 1:
        total = num1 + num2 + num3
        print "The total is: " + str(total)


### --- run code --- ###

calculate_total(1,2,-3)
calculate_total(1,2,3)
calculate_total(-10,2,3)
