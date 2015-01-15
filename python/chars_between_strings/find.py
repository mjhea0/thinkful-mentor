"""

Brute Force Attempt:

1. Convert string to list
2. Add a counter, initially set to 0
3. Loop through list, testing if the list element == the sub-string
    4. If True, add the value of the counter to a new list
    5. If False, iterate the counter
6. Return the list

"""


def find_characters_between(string, sub_string):
    answer_array = []
    all_strings = string.split()
    print all_strings
    element_counter = 0
    for string in all_strings:
        if string == sub_string:
            answer_array.append(element_counter)
            element_counter = 0
        else:
            element_counter += 1
    return answer_array


# Test 1
string_one = '20 43 DA 4e 4e 45 43 DA 45 44 20 DA 20 20 20 DA'
sub_string_one = 'DA'
print find_characters_between(string_one, sub_string_one) == [2, 4, 3, 3]

# Test 2
string_two = '20 43 DA 4e 4e 45 43 DA 45 44 20 DA 20 20 20 DA'
sub_string_two = '43'
print find_characters_between(string_two, sub_string_two) == [1, 4]

# Test 3
string_two = """99 bottles of beer on the wall 99 bottles of beer
Take one down and pass it around 98 bottles of beer on the wall"""
sub_string_two = 'beer'
print find_characters_between(string_two, sub_string_two) == [3, 6, 10]
