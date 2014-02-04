import time
import pdb

def debugging_code(num_list):
    t1 = time.time()
    pdb.set_trace()
    num_list.sort()
    largest_num = num_list[-1:][0]
    t2 = time.time()
    output = []
    output.extend([largest_num,(t2-t1)])
    return output 

my_list = debugging_code([1,9,13,16,0,8,18,6])

print "This program took " + str(my_list[1]) + " to run, \
and the largest number is " + str(my_list[0]) + "."

