import sys

def correct_num(number):
    """
    loop until user enters the correct number
    """
    try:
        assert number == 0
    except AssertionError:
        print "\nOops! That was not a valid number. Try again.\n"
        while True:
            try:
                number = int(raw_input("Please enter a number: "))
                assert number == 0
                break
            except AssertionError:
                print "\nOops! That was not a valid number. Try again.\n"
 
 
def main():
    num = int(sys.argv[1])
    correct_num(num)

 
if __name__ == '__main__':
    main()
