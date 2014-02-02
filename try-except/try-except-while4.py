# needs to be refactored

import sys

def calculate_total(meal_price):
    """
    loop until user enters the correct number
    """
    while True:
        try:
            meal_price > 0
            break
        except AssertionError:
            print "\nOops! The meal price must be > $0. Try again.\n"
            try:
                new_meal_price = float(raw_input("Please enter the cost of the meal: "))
                assert new_meal_price > 0
                print "Meal: ${:.2f}".format(new_meal_price)
                break
            except AssertionError:
                print "\n"


def main():
    meal = float(sys.argv[1])
    calculate_total(meal)
 
if __name__ == '__main__':
    main()
