# needs to be refactored

import sys

def correct_num(number):
    """
    loop until user enters the correct number
    """
    while True:
        try:
            assert number == 0
            break
        except AssertionError:
            print "\nOops! That was not a valid number. Try again.\n"
            try:
                num = int(raw_input("Please enter a number: "))
                assert num == 0
                break
            except AssertionError:
                print "\n"
 
 
def main():
    num = int(sys.argv[1])
    correct_num(num)

 
if __name__ == '__main__':
    main()
