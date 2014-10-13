import logging
import sys

from src.parser import make_parser
from src.tweetful import get_friends, get_followers, get_timeline
from src.authorization import authorize


def main():
    """ Main function """
    logging.info("Tweetful -- starting main()")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)

    auth = authorize()

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
