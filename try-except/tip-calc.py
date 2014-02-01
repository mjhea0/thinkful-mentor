import sys

def assert_arguments(meal,tax,tip):
    """
    asserts that the arguments are are numbers (floats)
    if not, then uses raw_input to get new values
    """
    num_list = []
    while True:
        try:
            assert type(float(meal)) and type(float(tax)) and type(float(tip)) != str
            num_list.extend([float(meal),float(tax),float(tip)])
            return num_list
        except ValueError:
            print "\nOops! That was not a valid number. Try again.\n"
            meal = raw_input("Re-enter the cost of your meal (i.e., 10 = $10.00): ")
            tax = raw_input("Re-enter tax rate as a decimal (i.e., .12 = 12%): " )
            tip = raw_input("Reenter how much would you like to tip? (i.e., .20 = 20%): ")
                    

 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(list_of_values):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(list_of_values[0], list_of_values[1])
    meal_with_tax = tax_value + list_of_values[0]
    tip_value = calculate_rate(meal_with_tax, list_of_values[2])
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=list_of_values[0],
                    tax_rate=list_of_values[1],
                    tip_rate=list_of_values[2],
                    tip_value=tip_value,
                    tax_value=tax_value,
                    total = total)
    return meal_info
 
def main():
    # grab arguments
    meal = sys.argv[1]
    tax = sys.argv[2]
    tip = sys.argv[3]

    # run validation
    all_values = assert_arguments(meal,tax,tip)

    # calculate values
    meal_info = calculate_meal_costs(all_values)

    # output results
    print "\nThe base cost of your meal was ${0:.2f}.".format(meal_info['meal_base'])
    print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                        float(100*meal_info['tip_rate']), 
                                        meal_info['tip_value'])
    print "The grand total of your meal is ${0:.2f}.".format(meal_info['total']) + "\n"

if __name__ == '__main__':
    main()
