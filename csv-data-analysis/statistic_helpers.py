# helper functions


def calculate_median(list_data):
    """
    calculates mean from a list of numbers
    """
    list_data.sort()
    list_length = len(list_data)
    ceiling = list_data[list_length/2]
    floor = list_data[list_length/2-1]
    if list_length % 2 == 0:
        return (ceiling + floor) / 2
    else:
        return list_data[list_length/2]


# ---- run code ---- #

import numpy
import random

even_data = random.sample(range(1000), 100)
odd_data = random.sample(range(1000), 101)

print calculate_median(even_data) == numpy.median(even_data)
print calculate_median(odd_data) == numpy.median(odd_data)
