import logging
import csv
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def put(name, snippet, filename):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Writing {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")
    with open(filename, "a") as f:
        writer = csv.writer(f)
        logging.debug("Writing snippet to file".format(name, snippet))
        writer.writerow([name, snippet])
    logging.debug("Write successful")
    return name, snippet


def get(name, filename):
    """ Retrieves a snippet associated with the user-provided name """
    logging.info("Retrieving {} snippet from {}".format(name, filename))
    logging.debug("Opening file")
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[0] == name:
                # print row
                return name, row[1]
    return name, "ERROR"


def search(snippet, filename):
    """ Searches for a matching snippet and returns itself and the name """
    logging.info(
        "Searching {} for a snippet matching '{}'".format(filename, snippet))
    logging.debug("Opening file")
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[1] == snippet:
                return row[0], snippet


def modify(name, snippet, filename):
    """ Modifies an already-existing snippet """
    logging.info("Modifying {}:{} to {}".format(name, snippet, filename))
    logging.debug("Opening file")

    index = 0

    with open(filename, "r") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if row[0] == name:
                index = counter
                break
            counter += 1

    with open(filename, "r") as f:
        data = f.readlines()

    data[index] = name + ',' + snippet + '\n'

    with open(filename, 'w') as f:
        f.writelines(data)

    return name, snippet


def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    put_parser.add_argument(
        "filename", default="snippets.csv",
        nargs="?", help="The snippet filename")

    #Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieves a snippet")
    get_parser.add_argument("name", help="The name of the snippet")
    get_parser.add_argument(
        "filename", default="snippets.csv",
        nargs="?", help="The snippet filename")

    #Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser(
        "search", help="Searches for a snippet")
    search_parser.add_argument(
        "snippet", help="The snippet text")
    search_parser.add_argument(
        "filename", default="snippets.csv",
        nargs="?", help="The snippet filename")

    #Subparser for the modify command
    logging.debug("Constructing modify subparser")
    modify_parser = subparsers.add_parser("modify", help="Modifies a snippet")
    modify_parser.add_argument("name", help="The name of the snippet")
    modify_parser.add_argument("snippet", help="The snippet text")
    modify_parser.add_argument(
        "filename", default="snippets.csv",
        nargs="?", help="The snippet filename")

    return parser


def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    #print arguments
    #print arguments.__dict__

    #Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored '{}' as '{}'".format(snippet, name)
    elif command == "get":
        name, snippet = get(**arguments)
        if snippet == "ERROR":
            print "Could not find snippet for name '{}'".format(
                arguments["name"])
        else:
            print "Stored '{}' as '{}'".format(snippet, name)
    elif command == "search":
        try:
            name, snippet = search(**arguments)
            print "Stored '{}' as '{}'".format(snippet, name)
        except:
            print "Could not find '{}' snippet".format(arguments["snippet"])
    elif command == "modify":
        name, snippet = modify(**arguments)
        print "Modified '{}' to '{}' snippet".format(name, snippet)

if __name__ == "__main__":
    main()
