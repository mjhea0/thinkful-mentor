def correct_num():
    """
    loop until user enters the correct number
    """
    while True:
        try:
            num = int(raw_input("Please enter a number: "))
            assert num == 0
            break
        except AssertionError:
            print "Oops! That was not a valid number. Try again."

correct_num()
