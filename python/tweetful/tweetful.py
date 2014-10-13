from __future__ import unicode_literals
import authorization
import requests
import logging
import sys

from urls import *
from parser import make_parser

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def get_friends(auth):
    response = requests.get(GET_FRIENDS_URL, auth=auth)
    for user in response.json()["users"]:
        print user["screen_name"]


def get_followers(auth):
    response = requests.get(GET_FOLLOWERS_URL, auth=auth)
    for user in response.json()["users"]:
        print user["screen_name"]


def get_timeline(auth):
    response = requests.get(TIMELINE_URL, auth=auth)
    for post in response.json():
        print post["user"]["screen_name"]
        print post["text"].encode('ascii', 'ignore')


def main():
    """ Main function """
    logging.info("Tweetful -- starting main()")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)

    auth = authorization.authorize()

    if arguments['tweet']:
        print 'Tweeting "{}"'.format(arguments['tweet'])

    if arguments['info']:
        if arguments['info'] == "friends":
            get_friends(auth)

        if arguments['info'] == "followers":
            get_followers(auth)

        if arguments['info'] == "timeline":
            get_timeline(auth)


if __name__ == "__main__":
    main()
