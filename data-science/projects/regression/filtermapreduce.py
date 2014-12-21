mylist = [2]

'''
Filter calls the lambda function for each element
in the list and returns a new list that contains only
those elements for which the function returned "True".
Thus, it is basically filtering out the list.
'''
print filter(lambda x: x**2, mylist)

'''Map is used to convert the list into a new list.'''
print map(lambda x: x**2, mylist)

'''Reduce acts like a sum function.'''
print reduce(lambda x, y: x + y, mylist)
