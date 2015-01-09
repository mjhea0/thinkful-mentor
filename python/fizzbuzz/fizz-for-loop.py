# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for i in num_list:
#     if i % 15 == 0:
#         print "fizzbuzz"
#     elif i % 5 == 0:
#         print "fizz"
#     elif i % 3 == 0:
#         print "buzz"
#     else:
#         print i


for i in xrange(1, 100):
    if i % 15 == 0:
        print "fizzbuzz"
    elif i % 5 == 0:
        print "fizz"
    elif i % 3 == 0:
        print "buzz"
    else:
        print i
