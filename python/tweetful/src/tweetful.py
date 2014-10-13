from __future__ import unicode_literals
import requests
import logging

from .urls import GET_FRIENDS_URL, GET_FOLLOWERS_URL, TIMELINE_URL

# Set the log output file, and the log level
logging.basicConfig(filename="src/output.log", level=logging.DEBUG)


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
