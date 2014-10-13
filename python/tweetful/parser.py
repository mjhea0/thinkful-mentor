import argparse
import logging


def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Command line Twitter client"
    parser = argparse.ArgumentParser(description=description)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-i', '--info', type=str, choices=["followers", "friends", "timeline"],
        help="Display user information")
    group.add_argument('-t', '--tweet', type=str, help="Text to tweet")

    return parser
