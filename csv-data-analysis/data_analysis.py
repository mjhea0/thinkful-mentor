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