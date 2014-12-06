""" Basics of regexes. """

import re

print "DIVE INTO PYTHON"
print "EXAMPLE 7.1"

s = '100 NORTH MAIN ROAD'
print s.replace('ROAD', 'RD')

s = '100 NORTH MAIN BROAD ROAD'
print s.replace('ROAD', 'RD')

print s[:-4] + s[-4:].replace('ROAD', 'RD')

print re.sub("ROAD$", "RD", s)  #this one is useful, pass in s

##################################################################

print "\n\nEXAMPLE 7.2"

s = '100 BROAD'
print re.sub("ROAD$", "RD.", s)

s = '100 BROAD ROAD APT. 3'
print re.sub('\\bROAD', 'RD.', s)
print re.sub(r'\bROAD', 'RD.', s)  # good one. use raw strings to avoid backslash

####################

print "\n\nEXAMPLE 7.31"
"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""

pattern = '^M?M?M?$'
print re.search(pattern, 'M')
print re.search(pattern, 'MM')
print re.search(pattern, 'MMM')
print re.search(pattern, 'MMMM')
print re.search(pattern, '')


print "\n\nEXAMPLE 7.4"
pattern = "^M?M?M?(CM|CD|D?C?C?C?)$"
print re.search(pattern, 'MCM')
print re.search(pattern, 'MD')
print re.search(pattern, 'MMMCCC')
print re.search(pattern, 'MCMC')
print re.search(pattern, '')

###############################
print "\n\n EXAMPLE 7.6"
pattern = r"^M{0,3}$"
print re.search(pattern, 'M')
print re.search(pattern, 'MM')
print re.search(pattern, 'MMM')
print re.search(pattern, 'MMMM')
print re.search(pattern, '')


###############################
print '\n\n EXAMPLE 7.8'
pattern = r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print re.search(pattern, 'MDLV')            
print re.search(pattern, 'MMDCLXVI')         
print re.search(pattern, 'MMMMDCCCLXXXVIII') 
print re.search(pattern, 'I')                


###############
print '\n\n EXAMPLE 7.9'
pattern = r"""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """
print re.search(pattern, 'M', re.VERBOSE)

################
print '\n\n EXAMPLE 7.10'
pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print pattern.search("215-555-1234").groups()


print '\n\n EXAMPLE 7.12'
pattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})$')
print pattern.search("215 555 1234").groups()
print pattern.search("215.555.1234").groups()
print pattern.search("215-555-1234").groups()

print '\n\n EXAMPLE 7.13'
pattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})$')
print pattern.search("2155551234").groups()
print pattern.search("215-555-1234").groups()

