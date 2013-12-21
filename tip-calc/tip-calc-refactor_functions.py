# global variables
tax_rate =.0625
answer = 'yes'

# calculate after tax amount
def calculate_tax(cost, rate_of_tax):
    tax = (cost * rate_of_tax)
    after_tax = tax + cost
    return after_tax

# determine tip amount
def determine_tip(answer, cost, post_tax):
    # while loop
    while (answer=='yes' or answer=='y'):
        tip_percent = float(raw_input('How much would you like to tip (20 = 20%)? '))
        tip_percent_convert = tip_percent * .01
        tip_total = tip_percent_convert * cost
        total = tip_total + post_tax
        print "Tipping at a rate of %.2f percent, your grand total would be %.2f." % (tip_percent, total)
        answer = raw_input('Would you like to change your tip amount ("yes" or "no")? ')
        answer = answer.lower()
    return total

## ---- run code ---- ##

base = float(raw_input("How much did your meal cost? "))
after_tax = calculate_tax(base, tax_rate)
total = determine_tip(answer,base,after_tax)

print "\nThe grand total of your meal is $%.2f" % total
