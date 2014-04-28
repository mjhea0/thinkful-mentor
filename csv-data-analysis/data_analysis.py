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