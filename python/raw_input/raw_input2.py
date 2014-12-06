"""Basic raw_input with a regex."""

import re

fun = raw_input("Are you having fun? ")
if re.match("^yes$|^y$", fun, re.IGNORECASE):
    print "great"
else:
    print "sorry to hear that"