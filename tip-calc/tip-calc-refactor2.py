# global variables
base = float(raw_input("How much did your meal cost? ")) # change to float
tax_rate =.0625

# calculate tax
tax = (base * tax_rate)
after_tax = tax + base

# while loop
answer = 'yes'
while (answer=='yes' or answer=='y'):
    tip_percent = float(raw_input('How much would you like to tip (20 = 20%)? '))
    tip_percent_convert = tip_percent * .01
    tip_total = tip_percent_convert * base
    total = tip_total + after_tax
    print "Tipping at a rate of %.2f percent, your total would be %.2f." % (tip_percent, total)
    answer = raw_input('Would you like to change your tip amount ("yes" or "no")? ')
    answer = answer.lower()
    print answer

# total    
total = tip_total + after_tax

# output
print "\n"
print "The base cost of your meal was $%r." % base
print "You need to pay $%.2f for tax." % tax
print "Tipping at a rate of $%.2f, you should leave $%.2f for a tip." % (tip_percent, tip_total)
print "The grand total of your meal is $%.2f" % total
print "\n"
