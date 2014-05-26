import time

def timing_function(some_function):
    def wrapper():
        list_test = []
        t1 = time.time()
        x = some_function()
        t2 = time.time()
        return (t2-t1),x
    return wrapper

@timing_function
def my_function():
    num_list = []      
    for x in (range(0,10000)):
        num_list.append(x)
    return (sum(num_list))


print "\nnow calling the function ..."
print
x, y = my_function()
print x
print "----"
print y

