import time

def timing_function(some_function):
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2-t1)) + "\n"
    return wrapper

@timing_function
def my_function():
    num_list = []      
    for x in (range(0,10000)):
        num_list.append(x)
    print "\nSum of all the numbers: " +str((sum(num_list)))


print my_function()
