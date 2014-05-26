import re

# from sloppy_data import data


# pattern = re.sub(r'^\s*\n', ' ', data)

# print pattern

with open('sloppy_data.txt', 'r') as file:
    for line in file.readlines():
        re.search('\S', line)
        print line,
