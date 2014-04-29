import csv
import pandas
import numpy
import matplotlib.pyplot as plt
from statistic_helpers import calculate_median


my_file = 'us_arrests.csv'


def import_data(delimited_file):
    """
    imports the a delimited file and casts the data to a list
    """
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    """
    seperates the headings from the data
    """
    headings = data[0]
    data.pop(0)
    print pandas.DataFrame(data, columns=headings)


def get_basic_statistics(data):
    """
    grabs the values for a specific crime
    *function should be renamed*
    """
    murder = []
    for crime in data:
        murder.append(float(crime[1]))
    return murder


def calculate_statistics(crime):
    """
    calculates mean, media, and standard Deviation
    """
    return numpy.mean(crime), numpy.median(crime), numpy.std(crime)


def calculate_min_and_max(crime):
    """
    calculates min and max values
    """
    return numpy.min(crime), numpy.max(crime)


def get_state(crime, min_max, data):
    """
    associates the state with the min and max values
    """
    state = []
    min_index = crime.index(min_max[0])
    max_index = crime.index(min_max[1])
    for crime in data:
        state.append(crime[0])
    return state[min_index], state[max_index]


def create_frequency_distribution(crime):
    """
    creates a frequency distribution chart
    """
    hist, bin_edges = numpy.histogram(crime, bins=10)
    return hist, bin_edges


def create_histogram(crime):
    """
    creates a histogram in matplotlib
    """
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
    print calculate_median(murder) == numpy.median(murder)
    create_histogram(murder)