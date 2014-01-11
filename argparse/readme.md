# argparse

argparse is a module that allows for easy handling and parsing of command line options/arguments (argument sent to the program being called). You simply specify the required arguments and argparse will either parse the arguments, display a help message, or issue an error.

Let's jump right into an example ..

Code:

```python
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument("square", help="display a square of a given number", type=int)

# parse arguments
args = parser.parse_args()

# output results
print(args.square**2)
```

This simple program takes one argument, an integer, then returns the square:


```shell
$ python arg-ex1.py 9
81
```

Try accessing the help:

```shell
 python arg-ex1.py -h
usage: arg-ex1.py [-h] square

positional arguments:
  square      display a square of a given number

optional arguments:
  -h, --help  show this help message and exit
```

Finally, if you don't enter any arguments, you'll see an error:

```shell
$ python arg-ex1.py
usage: arg-ex1.py [-h] square
arg-ex1.py: error: too few arguments
```
