class Bill():

    # calculate after tax amount
    def calculate_tax(self, cost):
        tax_rate =.0625
        tax = (cost * tax_rate)
        after_tax = tax + cost
        return after_tax

    # determine tip amount
    def determine_tip(self, cost, post_tax):
        # while loop
        answer = "yes"
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

my_bill = Bill() # instantiate
base = float(raw_input("How much did your meal cost? "))
tax = my_bill.calculate_tax(base)
total = my_bill.determine_tip(base, tax)

print "\nThe grand total of your meal is $%.2f" % total
