import re

name = 'Michael Herman'

print name
print

for pattern in [r"(?P<first>\w+)",r"\W+(?P<last>\w+)"]:
    regex = re.compile(pattern)
    match = regex.search(name)
    print 'Matching "%s"' % pattern
    print '  ', match.groups()
    print
