base= int(raw_input("How much did your meal cost?"))
tax=.0625
taxtwo=(base*.0625)
after_tax= taxtwo + base
eric='yes'
while (eric=='yes'):
    tip_percent=float(raw_input('how much would you like to tip?'))
    tip_total=tip_percent*base
    total=tip_total+after_tax
    print "Tipping at a rate of %.2f, your total would be %.2f." % (tip_percent, total)
    eric=raw_input("Would you like to change your tip amount?")
    
total=tip_total+after_tax
print "\n"
print "The base cost of your meal was %r." % base
print "You need to pay %.2f for tax." % taxtwo
print "Tipping at a rate of %.2f, you should leave %.2f for a tip." % (tip_percent, tip_total)
print "The grand total of your meal is %.2f" % total
