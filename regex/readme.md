## Groups

By adding groups to a regular expression pattern you can further isolate portions of the matching text. You specify groups with parenthesis within the pattern. 

### Example

```python
import re

string = "My name is Michael Herman"

# re.match(pattern, string, flags=0)
m = re.match(r'(.*) name (.*?) .*', string)

if m:
   print "group(0) : ", m.group(0)
   print "group(1) : ", m.group(1)
   print "group(2) : ", m.group(2)
else:
   print "Sorry. No match!!"
```

Results:

```shell
group() :  My name is Michael Herman
group(1) :  My
group(2) :  is
```

#### What's going on?

Group 0 defines the string matched from the entire regular expression, while Group 1 and 2 represent sub-groups.

## Named Groups

You can also define groups names, which makes the groups easier to read.

### Example

```
import re

string = "Michael Herman"

# re.match(pattern, string, flags=0)
m = re.match("(?P<first>\w+)\W+(?P<last>\w+)", string)

if m:
   print "group(0) : ", m.group(0)
   print "group(1) : ", m.group(1)
   print "group(2) : ", m.group(2)
   print ""
   print 'group("first") : ', m.group("first")
   print 'group("last") : ', m.group("last")   
else:
   print "Sorry. No match!!"
```

Results:

```shell
group(0) :  Michael Herman
group(1) :  Michael
group(2) :  Herman

group("first") :  Michael
group("last") :  Herman
```

#### What's going on?

Group 0 defines the string matched from the entire regular expression, while Group 1 and 2 still represent the sub-groups. Since we also added in named groups, we can also respresent the substrings with "first" and "last".



