# needs to be refactored

import sys

def calculate_total(meal_price):
    """
    loop until user enters the correct number
    """
    try:
        assert meal_price > 0
        return meal_price
    except AssertionError:
        print "\nOops! The meal price must be > $0. Try again.\n"
        while True:
            try:
                meal_price = float(raw_input("Please enter the cost of the meal: "))
                assert meal_price > 0
                return meal_price
            except AssertionError:
                print "\nOops! The meal price must be > $0. Try again.\n"


def main():
    meal = float(sys.argv[1])
    price = calculate_total(meal)
    print "Meal: ${:.2f}".format(price)
 
if __name__ == '__main__':
    main()
