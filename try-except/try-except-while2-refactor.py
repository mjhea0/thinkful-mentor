import sys

def correct_num():
    """
    loop until user enters the correct number
    """
    try:
        num = int(sys.argv[1])
        assert num == 0
    except AssertionError:
        while num != 0:
            print "\nOops! That was not a valid number. Try again.\n"
            num = int(raw_input("Please enter a number: "))

correct_num()
