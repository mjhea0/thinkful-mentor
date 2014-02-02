def foo(bar):
 return bar + 1

def baz(qux):
  return qux + 1


num = foo(2)
print baz(num) == 4

# OR #

print baz(foo(2)) = 4
