from __future__ import print_function

def iterate(l, fn):
    for x in l:
        result = fn(x)
        print ("{} ".format(result)),

nums = [1, 2, 3, 4, 5]

iterate(nums, lambda x: x * x) # square

print("")

iterate(nums, lambda x: x + 5) # add 5

print("")

def printme(n):
    print ("hup {} ".format(n)), 
map(printme, nums)

print("")


map( lambda x: print("bup {} ".format(x)), nums)


#see also filters in unit 99
