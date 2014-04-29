# Python for Data Analysis: Analyzing CSV Data with Numpy, Pandas, and Matplotlib

In this intro tutorial, we're going to analyze a small dataset of the [U.S. crime rate](https://github.com/mjhea0/thinkful-mentor/blob/master/csv-data-analysis/us_arrests.csv) broken down by state using **[Numpy](http://www.numpy.org/)**, **[Pandas](http://pandas.pydata.org/)**, and [Matplotlib](http://matplotlib.org/). After importing and organizing the data, we'll calculate some summary statistics as well as provide a graphical display of the data itself.

## Importing CSV Data

Before beginning open up the CSV file in Excel or a text editor (or just view the link above) to see how it's organized, the data types, and the delimiter used for separating the data. 

![csv_data_us_crimes](https://raw.githubusercontent.com/mjhea0/thinkful-mentor/master/csv-data-analysis/img/csv_data_us_crimes.png)

Essentially, we're working with strings, integers, and floats, separated by commas. Now, let's start by importing the data in a Python-friendly format using the CSV library:

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
[['State,"Murder","Assault","UrbanPop","Rape"'], ['Alabama,13.2,236,58,21.2'], 
['Alaska,10,263,48,44.5'], ['Arizona,8.1,294,80,31'], ... ]
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

The `pop()` method removes an item from a list, which in this case is the 0-th element (the header list). This also removes the headers from our main list, seperating the headers from the *actual* data. You should now have two lists, assigned to two variables, `headings` and `data`.

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

Before we look at Pandas, you could use pretty-print to at least make the list legible:

```python
def seperate_headings_from_data(data):
    import pprint
    headings = data[0]
    data.pop(0)
    pp = pprint.PrettyPrinter(indent=4)
    print headings
    print "\n#-----------------------------------#\n"
    pp.pprint(data)
```

Test this out. Looks better, right. Well, Pandas makes it even easier to print the data in tabular format.

Simply install Pandas with pip:

```
$ pip install pandas
```

Then import the library and update the function:

```python
def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print pandas.DataFrame(data, columns=headings)
```

The [`DataFrame()`](http://pandas.pydata.org/pandas-docs/version/0.13.1/generated/pandas.DataFrame.html) class outputs the data in a nice table. We also used our `headings` list for the optional `columns` argument. 

![pandas_dataframe_ouput](http://pandas_dataframe_ouput.png)

## Basic Statistical Analysis with Numpy

Let's start with some summary statistics - e.g., the min, max, mean, median, and standard deviation. We'll look just at murder to simplify things.

First, install Numpy if you don't already have it:

```
$ pip install numpy
```

Next, we need to create a list for all of the murder rates:

```python
def get_basic_statistics(data):
    murder = []
    for crime in data:
        murder.append(float(crime[1]))
    return murder
```

Here, we're just using a `for` loop to iterate through the data and then grabbing the murder list using basic list manipulation. Simple, right? Then we return the new list.

Updated code:

```python
import csv
import pandas
import numpy

my_file = 'us_arrests.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print pandas.DataFrame(data, columns=headings)


def get_basic_statistics(data):
    murder = []
    for crime in data:
        murder.append(float(crime[1]))
    return murder


data = import_data(my_file)
seperate_headings_from_data(data)
get_basic_statistics(data)
```

Now let's use Numpy to sumarize the murder rate using two new functions:

```python
def calculate_statistics(crime):
    return numpy.mean(crime), numpy.median(crime), numpy.std(crime)

def calculate_min_and_max(crime):
    return numpy.min(crime), numpy.max(crime)
```

If you print the outputs, you should see a two tuples - one with the mean, median, and standard deviation, and the second with the min and max values:

```
(7.7879999999999994, 7.25, 4.3117346857152512)
(0.80000000000000004, 17.399999999999999)
```

Add `main()` and output stats:

```python
import csv
import pandas
import numpy

my_file = 'us_arrests.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print pandas.DataFrame(data, columns=headings)


def get_basic_statistics(data):
    murder = []
    for crime in data:
        murder.append(float(crime[1]))
    return murder


def calculate_statistics(crime):
    return numpy.mean(crime), numpy.median(crime), numpy.std(crime)


def calculate_min_and_max(crime):
    return numpy.min(crime), numpy.max(crime)


if __name__ == '__main__':
    data = import_data(my_file)
    seperate_headings_from_data(data)
    murder = get_basic_statistics(data)
    stats = calculate_statistics(murder)
    print "\nMurder Statistics"
    print "-----------------"
    print "Mean: {}".format((stats)[0])
    print "Median: {}".format((stats)[1])
    print "Std. Deviation: {}".format((stats)[2])
```

What are we missing? The min and max values as well as their respective states. The question is: How do we the min and max back to their respective U.S. states? 

We need to the grab the index of each value, then pass those values into a new list that includes each state:

```python
def get_state(crime, min_max, data):
    state = []
    min_index = crime.index(min_max[0])
    max_index = crime.index(min_max[1])
    for crime in data:
        state.append(crime[0])
    return state[min_index], state[max_index]
```

Update:

```python
import csv
import pandas
import numpy

my_file = 'us_arrests.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print pandas.DataFrame(data, columns=headings)
    

def get_basic_statistics(data):
    murder = []
    for crime in data:
        murder.append(float(crime[1]))
    return murder


def calculate_statistics(crime):
    return numpy.mean(crime), numpy.median(crime), numpy.std(crime)


def calculate_min_and_max(crime):
    return numpy.min(crime), numpy.max(crime)


def get_state(crime, min_max, data):
    state = []
    min_index = crime.index(min_max[0])
    max_index = crime.index(min_max[1])
    for crime in data:
        state.append(crime[0])
    return state[min_index], state[max_index]

if __name__ == '__main__':
    data = import_data(my_file)
    seperate_headings_from_data(data)
    murder = get_basic_statistics(data)
    stats = calculate_statistics(murder)
    min_max = calculate_min_and_max(murder)
    states = get_state(murder, min_max, data)
    print "\nMurder Statistics"
    print "-----------------"
    print "Mean: {}".format((stats)[0])
    print "Median: {}".format((stats)[1])
    print "Std. Deviation: {}".format((stats)[2])
    print "Highest crime rate: {} with a rate of {}".format(
        (states)[0], (min_max)[0])
    print "Lowest crime rate: {} with a rate of {}".format(
        (states)[1], (min_max)[1])
```

## Charting Data with Matplotlib

Now, let's quickly look at how to create a nice chart with Matplotlib. Perhaps you would like to see a histogram (a plot type used to show the frequency across a continuous or discrete variable) of the state murder rates. We can use the matplotlib.pyplot package's [`hist()`](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist) function for this. Make sure to install [Matplotlib](http://matplotlib.org/downloads.html).

Before creating thr histrogram, let's first use Numpy to create a frequency distribution:

```python
def create_frequency_distribution(crime):
    hist, bin_edges = numpy.histogram(crime, bins=10)
    return hist, bin_edges
```

Call this function and you should see the following output:

```
(array([5, 8, 5, 9, 6, 3, 5, 4, 3, 2]), array([  0.8 ,   2.46,   4.12,   5.78,   7.44,   9.1 ,  10.76,  12.42,
        14.08,  15.74,  17.4 ]))
```

This means that there are 5 states that have a murder rate between 0.8 and 2.46, 8 states that have a rate between 2.46 and 4.12, and so on.

Now, let's graph it:

```python
def create_histogram(crime):
    plt.hist(crime, facecolor='green', label='murders')
    plt.title("Murder Rate Histogram")
    plt.xlabel("murder rates")
    plt.ylabel("# of murders")
    plt.legend()
    plt.show() 
```

Final code:

```python
import csv
import pandas
import numpy
import matplotlib.pyplot as plt


my_file = 'us_arrests.csv'


def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    headings = data[0]
    data.pop(0)
    print pandas.DataFrame(data, columns=headings)


def get_basic_statistics(data):
    murder = []
    for crime in data:
        murder.append(float(crime[1]))
    return murder


def calculate_statistics(crime):
    return numpy.mean(crime), numpy.median(crime), numpy.std(crime)


def calculate_min_and_max(crime):
    return numpy.min(crime), numpy.max(crime)


def get_state(crime, min_max, data):
    state = []
    min_index = crime.index(min_max[0])
    max_index = crime.index(min_max[1])
    for crime in data:
        state.append(crime[0])
    return state[min_index], state[max_index]


def create_frequency_distribution(crime):
    hist, bin_edges = numpy.histogram(crime, bins=10)
    return hist, bin_edges


def create_histogram(crime):
    plt.hist(crime, facecolor='green', label='murders')
    plt.title("Murder Rate Histogram")
    plt.xlabel("murder rates")
    plt.ylabel("# of murders")
    plt.legend()
    plt.show() 


if __name__ == '__main__':
    data = import_data(my_file)
    seperate_headings_from_data(data)
    murder = get_basic_statistics(data)
    stats = calculate_statistics(murder)
    min_max = calculate_min_and_max(murder)
    states = get_state(murder, min_max, data)
    print "\nMurder Statistics"
    print "-----------------"
    print "Mean: {}".format((stats)[0])
    print "Median: {}".format((stats)[1])
    print "Std. Deviation: {}".format((stats)[2])
    print "Highest crime rate: {} with a rate of {}".format(
        (states)[0], (min_max)[0])
    print "Lowest crime rate: {} with a rate of {}\n".format(
        (states)[1], (min_max)[1])
    print create_frequency_distribution(murder)
    create_histogram(murder)
```





