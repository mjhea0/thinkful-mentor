import sys

def correct_num():
    """
    loop until user enters the correct number
    """
    while True:
        try:
            num = int(sys.argv[1])
            assert num == 0
            break
        except AssertionError:
            print "\nOops! That was not a valid number. Try again.\n"
            try:
                num = int(raw_input("Please enter a number: "))
                assert num == 0
                break
            except AssertionError:
                print "\n"

correct_num()
