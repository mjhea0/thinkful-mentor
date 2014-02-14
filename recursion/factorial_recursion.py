# recursive

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

def fact_loop(x):
    f = 1
    while (x > 0):
        f = f * x
        x = x - 1
    return f

#### ---- run code ---- ####

print fact(3) == 6
print fact(5) == 120
print fact(1) == 1

print fact_loop(3) == 6
print fact_loop(5) == 120
print fact_loop(1) == 1


#### --- decorator ---- ####

import time, random

def timing_function(some_function):
    def wrapper(num):
        t1 = time.time()
        some_function(num)
        t2 = time.time()
        return "Time it took to run the function: " + str((t2-t1)) + "\n"
    return wrapper


@timing_function
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)


@timing_function
def fact_loop(x):
    f = 1
    while (x > 0):
        f = f * x
        x = x - 1
    return f

print fact(5)
print fact_loop(5)

# @timing_function
# def my_function():
#     new_list = []
#     i = 0
#     while i < 10000:
#         for x in xrange(0,100):
#             new_list.append(x+random.randint(0,10))
#         i += 1

# print my_function()

