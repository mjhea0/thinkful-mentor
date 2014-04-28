# Python for Data Analysis: Analyzing CSV Data with Numpy and Pandas

In this tutorial, we're going to analyze a small dataset of the [U.S. crime rate](http://link) broken down by state using Numpy and Pandas. After importing and organizing the data, we'll calculate some summary statistics as well as provide a graphical display of the data itself.

## Importing CSV Data

Before beginning open up the CSV file in Excel or a text editor to see how it's organized, the data types, and the type of delimiter used for separating the data. Essentially, we're working with strings, integers, and floats, separated by commas. Now, let's create a simple script to read the data using the CSV library:

```python
import csv


my_file = 'us_arrests.csv'

def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
        print all_data

import_data(my_file)
```

Save this as *import_delimited_data.py* then run it. This should give you all of the rows of the dataset wrapped in a list:

```
[['State,"Murder","Assault","UrbanPop","Rape"'], ['Alabama,13.2,236,58,21.2'], ['Alaska,10,263,48,44.5'], ['Arizona,8.1,294,80,31'], ... ]
```

