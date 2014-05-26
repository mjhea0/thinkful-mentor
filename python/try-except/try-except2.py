# try/except example

def assert_positive(num):
    """assert that each number is greater than 0"""
    try:
        assert num > 0
        float(num)
    except AssertionError:
        print "Sorry. " + str(num) + " is less than zero. Try again."
        return 1
    except ValueError:
        print "Sorry. " + str(num) + " is not a number. Try again."
        return 1
    else: 
        return 0


def calculate_total(num1,num2,num3):
    """calculate total from three numbers"""
    num_list = []
    test = []
    num_list.extend((num1, num2, num3))
    for num in num_list:
        test.append(assert_positive(num))
        if len(test) == 3 and sum(test) == 0:
            total = sum(num_list)
            print "The total is: " + str(total)


### --- run code --- ###

calculate_total(1,2,-3)
calculate_total(1,2,3)
calculate_total(1,-20,3)
calculate_total(1,-2,"test")
