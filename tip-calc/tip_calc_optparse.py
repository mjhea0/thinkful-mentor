# Tip calculator code using optparse

from optparse import OptionParser

# create an instance of the OptionParser object
parser = OptionParser()

# create values for meal, tax, and tip using the parser.add_option() method
parser.add_option("-f", "--first", dest="meal", help="meal value", type="float")
parser.add_option("-s", "--second", dest="tax", help="tax %", type="float")
parser.add_option("-t", "--third", dest="tip", help="tip %", default="4.5", type="float")

(options, args) = parser.parse_args()

# raise error message if no meal value or tax% supplied
if not options.meal or not options.tax:
    parser.error("\nYou need to enter a value for the meal and tax - i.e., \n`python tip_calc_optparse.py -f [meal value] -s [tax %]`")

# assign the tax * meal to the variable tax_value
tax_value = options.meal * (options.tax / 100.0)

# assign tax_value + meal to variable meal_with_tax
meal_with_tax = tax_value + options.meal

# assign the value of tip% * meal_with_tax to variable tip_value
tip_value = meal_with_tax * (options.tip / 100.0)

# assign meal_with_tax + tip_value to variable total
total = meal_with_tax + tip_value

# print the cost of the meal
print "The cost of your meal is ${0:.2f}".format(options.meal)

# print the $ tax value
print "The tax on your meal is ${0:.2f} or {1}%".format(tax_value, options.tax)

# print the $ tip value and tip rate
print "You need to pay ${0:.2f} in tips based on {1}% tip rate".format(tip_value, options.tip)

# print total for meal
print "The grand total for your meal comes to ${0:.2f}".format(total)