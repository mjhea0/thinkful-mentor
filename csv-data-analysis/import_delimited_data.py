import csv


my_file = 'us_arrests.csv'

def import_data(delimited_file):
    with open(delimited_file, 'rb') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
        print all_data

import_data(my_file)