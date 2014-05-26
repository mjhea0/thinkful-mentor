## Attribute Error - 'NoneType' object has no attribute 'something'

`NoneType` means that instead of an instance of whatever Class or Object you think you're working with, you've actually got `None`. That usually means that an assignment or function call up above failed or returned an unexpected result.

### Example 

```sh
>>> foo = None
>>> foo.something = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'something'
```

### Example

```sh
>>> my_list = [1,4,5,6]
>>> my_list = my_list.sort()
>>> my_list.append(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'append'
```

The sort() method of a list sorts the list in-place - but the actual return value of the method is None and not the sorted list. So you've just assigned None to mylist. If you next try to do, say, mylist.append(1) Python will give you this error.
