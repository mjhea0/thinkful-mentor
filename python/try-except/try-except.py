# try/except example

def assertions(num_list):
    for num in num_list:
        try:
            assert num > 0
            total = 1 + 2 + 3
        except AssertionError:
            return "sorry, " + str(num) + " is less than zero."
    return total



# num_list = [1,2,3]
num_list = [1,2,-3]
print assertions(num_list)



