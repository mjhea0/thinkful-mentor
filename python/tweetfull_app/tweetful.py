import authorization
import requests
from urls import TIMELINE_URL, UPDATE_URL, REVERSE_GEOCODE_URL, TRENDS_URL
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

def get_timeline(auth):
    response = requests.get(TIMELINE_URL, auth=auth)
    return response.json()

def post_to_timeline(auth, message):
    payload = dict(status=message)
    response = requests.post(UPDATE_URL, auth=auth, 
        params=payload)
    return response.json()

def geocode(auth, lat, lon):
    payload = dict(lat=lat, long=lon)
    response = requests.get(REVERSE_GEOCODE_URL, auth=auth, 
        params=payload)
    j = response.json()
    
    name = None
    woeid = None
    try:
        name =  j["result"]["places"][0]["name"]
        woeid = j["result"]["places"][0]["id"]
    except:
        print "Did not get the right data from get_woeid"
    
    return name, woeid


def get_top_tweets(auth, woeid):
    #print "trying to get trends for woeid = {}".format(woeid)
    payload = {"id": woeid}
    #print TRENDS_URL
    response = requests.get(TRENDS_URL, auth=auth, 
        params=payload)
    return response.json()
    
def print_trends(trends):
    for t in trends[0]["trends"]:
        print t["name"]

def main():
    """ Main function """
    auth = authorization.authorize()

    """Get timeline"""
    #print get_timeline(auth)
    
    """Post to timeline"""
    #print post_to_timeline(auth, "hello twitter api")

    """Top Trends"""


    """http://woeid.rosselliot.co.nz/"""
    woeids = dict(
        gaza = 1979608
        #philadelphia = 2471217
        #brasilia = 455819,
        #telaviv = 1968212,
        #ramahlla = 1937180
    )
    
    
    for place, woeid in woeids.iteritems():
        print "\n" + place.upper()
        trends = get_top_tweets(auth, woeid)
        print_trends(trends)

    # print "\n\nBRASILIA"
    # trends = get_top_tweets(auth, brasilia)
    # print_trends(trends)

    # print "\n\nTEL AVIV"
    # trends = get_top_tweets(auth, telaviv)
    # print_trends(trends)

    # print "\n\nRamahlla"
    # trends = get_top_tweets(auth, ramahlla)
    # pp.pprint(trends)



if __name__ == "__main__":
    main()


