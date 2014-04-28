# Python for Data Analysis: Analyzing CSV Data with Numpy and Pandas

In this intro tutorial, we're going to analyze a small dataset of the [U.S. crime rate](http://link) broken down by state using Numpy and Pandas. After importing and organizing the data, we'll calculate some summary statistics as well as provide a graphical display of the data itself.

## Importing CSV Data

Before beginning open up the CSV file in Excel or a text editor to see how it's organized, the data types, and the type of delimiter used for separating the data. Essentially, we're working with strings, integers, and floats, separated by commas. Now, let's start by importing the data in a Python-friendly format using the CSV library:

```python
import csv


my_file = 'us_arrests.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data

print import_data(my_file)
```

Save this as *data_analysis.py* then run it. This should give you all of the rows of the dataset wrapped in a list:

```
[['State,"Murder","Assault","UrbanPop","Rape"'], ['Alabama,13.2,236,58,21.2'], ['Alaska,10,263,48,44.5'], ['Arizona,8.1,294,80,31'], ... ]
```

The first row, `all_data[0]` contains the headings. Let's seperate the headings from the data to make analysis easier with another function:

```python
def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print headings
    print "\n#-----------------------------------#\n"
    print data
```

The `pop()` method removes an item from a list, which in this case is the 0-th element (the header list). This also removes the headers from our main lisr, seperating the headers from the *actual* data. You should now have two lists, assigned to two variables.

Updated code:

```python
import csv


my_file = 'us_arrests.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print headings
    print "\n#-----------------------------------#\n"
    print data

data = import_data(my_file)
seperate_headings_from_data(data)
```

## Displaying Data with Pandas

