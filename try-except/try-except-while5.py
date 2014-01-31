# easier with if statements?

import sys

def calculate_total(meal_price):
    """
    loop until user enters the correct number
    """
    if meal_price > 0:
        return meal_price
    else:
        while meal_price < 0:
            print "The meal cost must be greater than $0. Try again."
            meal_price = float(raw_input("Please enter the cost of the meal: "))
        return meal_price


def main():
    meal = float(sys.argv[1])
    meal_price = calculate_total(meal)
    print "Meal: ${:.2f}".format(meal_price)
 
if __name__ == '__main__':
    main()
