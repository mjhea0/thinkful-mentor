# Interlude: Regular Expressions

Regular expressions (also known as regex) provide a powerful syntax for pattern matching used to extract information from text documents.

## When should you use regular expressions?

Unless you absolutely need to use regular expressions, stick with Python basic string functions - like `find` and `replace`. They are *much* easier to learn, use, and understand.

However, these are generally only useful when you know *exactly* what you're looking for.

For example:

```sh
>>> str = 'Explicit is better than implicit.'
>>> print text.find('implicit')
24
```

But what happens if we don't know *exactly* what we're looking for, such as a 10-digit phone number. In that case, we only know that the pattern is an integer, with 10-digits (that may or may not be seperated by a dash or some other character). This is the perfect use case for regex:

```sh
>>> import re
>>> str = "Jack's phone number is 415-690-4993"
>>> phone = re.search(r'\d{3}\D*\d{3}\D*\d{4}$', str)
>>> print phone.group()
415-690-4993
```

Here, we have the regular expression `r'(\d{3})\D*(\d{3})\D*(\d{4})$'`, which includes three sub expressions:

1. `d{3}` matches any three digits
2. `D*` matches any non-digit
3. `d{4}` matches any four digits

> Check out [https://pythex.org/](https://pythex.org/) for a nice regex cheatsheet. You can also test expressions and patterns out. Click [here](https://pythex.org/?regex=%5Cd%7B3%7D%5CD*%5Cd%7B3%7D%5CD*%5Cd%7B4%7D&test_string=415-680-5773&ignorecase=0&multiline=0&dotall=0&verbose=0) to view the results of the above example.

What if you have an entire list of phone numbers that need to be standardized into the following format xxxxxxxxxx - and the numbers are in any one of these formats:

1. 555-555-5555
2. 555 555 5555
3. 555.555.5555
4. (555) 555-5555
5. (555)555-5555
6. (555)555.5555

Let's write a quick program to do this.

```python
import re

phone_list = ["555-555-5555","555 555 5555","555.555.5555",
    "(555) 555-5555","(555)555-5555","(555)555.5555"]

pattern = r'\D'

for phone in phone_list:
    phone_num = re.sub(pattern, "", phone)    
    print "Phone Num : ", phone_num
```

Let's look at another quick example.

```python
import re

email_list = ["my@email.com", "@email.com", "my@email"]

pattern = "^[A-Za-z0-9.]+@[A-Za-z0-9.]+.com$"

for email in email_list:
    test = re.findall(pattern, email)    
    print test
```

Here, we are given a list of email addresses, and we are just confirming whether they match the correct pattern - e.g., *something@something.com*.

So, although these are just basic examples, you should understand what a regular is and how to use them. Used correctly, in the right situation, you can save much time when having to parse a string. For further information, please check out these guides and tutorials:

1. [TutorialsPoint Regular Expressions](http://www.tutorialspoint.com/python/python_reg_expressions.htm)
2. [Python Course: Regular Expressions](http://www.python-course.eu/re.php)
3. [Python Module of the Week - re](http://pymotw.com/2/re/)
4. [http://www.pythonschool.net/regex](http://www.pythonschool.net/regex)
