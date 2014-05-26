# functions

"""
Directions: Convert into two functions. One function (called calculate_total) 
should calculate the sum of three numbers passed in, while the other 
function (assert_positive) checks to make sure that all the numbers in the list 
are positive.

Test each of these:
calculate_total(1,2,-3)
calculate_total(1,2,3)
calculate_total(-10,2,3)

One Answer: https://github.com/mjhea0/thinkful-mentor/blob/master/try-except/try-except2.py
Another Answer: 

"""

num_list = [1,2,3]
for num in num_list:
    try:
        assert num > 0
    except AssertionError:
        print "Sorry. " + str(num) + " is less than zero. Try again"
    else:
        total = sum(num_list)
print "The total is: " + str(total)
