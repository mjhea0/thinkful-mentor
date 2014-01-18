# refactor using the continue statement

def no_more_nests(array, array2):
    array_for_testing = []
    for num1, num2 in zip(array, array2):
        if num1 > num2:
            big_number = calculate_big_number(num1, num2)
            if num2 - big_number < num1:
                num2 = min(num2, big_number)
                if num1 ** 2 - num2 ** 2 > 0:
                    new_number = num2 * num1
                    for n in range(1,new_number):
                        while n > 300:
                            array_for_testing.append(n)
                            break
                    why = "Why is this getting outputted?"
                    array_for_testing.append(why)
    return array_for_testing

def calculate_big_number(number1, number2):
    new_number_that_is_bigger = number1 * number2
    return new_number_that_is_bigger



# ----- Run Code ---- #

evens_odds = [1,12,3,14,5,16,7,18,9,20]
odds_evens = [2,11,4,13,6,15,8,17,10,19]

print no_more_nests(evens_odds, odds_evens) == ['Why is this getting outputted?', 
                                                'Why is this getting outputted?', 
                                                'Why is this getting outputted?', 
                                                301, 302, 303, 304, 305, 
                                                'Why is this getting outputted?', 
                                                301, 302, 303, 304, 305, 306, 307, 
                                                308, 309, 310, 311, 312, 313, 314, 
                                                315, 316, 317, 318, 319, 320, 321, 
                                                322, 323, 324, 325, 326, 327, 328, 
                                                329, 330, 331, 332, 333, 334, 335, 
                                                336, 337, 338, 339, 340, 341, 342, 
                                                343, 344, 345, 346, 347, 348, 349, 
                                                350, 351, 352, 353, 354, 355, 356, 
                                                357, 358, 359, 360, 361, 362, 363, 
                                                364, 365, 366, 367, 368, 369, 370, 
                                                371, 372, 373, 374, 375, 376, 377, 
                                                378, 379, 
                                                'Why is this getting outputted?']
