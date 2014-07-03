from collections import OrderedDict
import json


# nice way to visualize data
with open('data.json') as json_file:
    json_data = json.load(json_file, object_pairs_hook=OrderedDict)

    print json.dumps(json_data, indent=2)

print "\n"
print "-----" * 4
print "\n"

# single url
with open('data.json') as json_file:
    json_data = json.load(json_file)

    for data in json_data:
        print json_data[0]["trends"][0]["url"]

print "\n"
print "-----" * 4
print "\n"

# all urls
with open('data.json') as json_file:
    json_data = json.load(json_file)

    for data in json_data:
        for value in json_data[0]["trends"]:
            print value["url"]


"""
1. Start with entire JSON object
2. Since it's wrapped in a list, iterate through it with a for loop
3. Next, work your way to the inner key ('trends') that contains the url
4. Loop through the values and output the 'url'
"""
