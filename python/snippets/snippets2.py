#!/usr/bin/env python

import sys
import argparse
import logging
import psycopg2

logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets' host='localhost'")
logging.debug("Database connection established.")

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def get(name):
    """ Print a snippet from a CSV file, based on an associated name. """
    logging.info("Reading snippet {!r}".format(name))
    cursor = connection.cursor()
    command = "select message from snippets where keyword='{}'".format(name)
    cursor.execute(command)
    return name, cursor.fetchone()[0]


def put(name, snippet):
    """ Store a snippet with an associated name in the CSV file """
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet


def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Store and retrieve snippets of text"
    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers(
        dest="command", help="Available commands")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Print a snippet")
    get_parser.add_argument("name", help="The name of the snippet")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")

    return parser


def main():
    """ Main function """
    logging.info("Starting snippets")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "get":
        name, snippet = get(**arguments)
        if snippet:
            print "Retrieved '{}', keyed to '{}'".format(snippet, name)

        else:
            print "ERROR: Unable to find any snippets keyed to '{}'.".format(
                name)

    if command == "put":
        name, snippet = put(**arguments)
        print "Stored '{}' as '{}'".format(snippet, name)


if __name__ == "__main__":
    main()
