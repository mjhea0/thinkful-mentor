import urlparse

import requests
from requests_oauthlib import OAuth1

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *
import json


def store_credentials(access_token, access_secret):
    """ Save our access credentials in a json file """
    with open("access.json", "w") as f:
        json.dump({"access_token": access_token,
                   "access_secret": access_secret}, f)


def get_stored_credentials():
    """ Try to retrieve stored access credentials from a json file """
    with open("access.json", "r") as f:
        credentials = json.load(f)
        return credentials["access_token"], credentials["access_secret"]


def get_request_token():
    """ Get a token allowing us to request user authorization """
    oauth = OAuth1(CLIENT_KEY, client_secret=CLIENT_SECRET)
    response = requests.post(REQUEST_TOKEN_URL,
                             auth=oauth)
    credentials = urlparse.parse_qs(response.content)

    request_token = credentials.get("oauth_token")[0]
    request_secret = credentials.get("oauth_token_secret")[0]
    return request_token, request_secret


def authorize():
    """ A complete OAuth authentication flow """
    try:
        access_token, access_secret = get_stored_credentials()
    except IOError:
        request_token, request_secret = get_request_token()
        verifier = get_user_authorization(request_token)
        access_token, access_secret = get_access_token(request_token,
                                                       request_secret,
                                                       verifier)
        store_credentials(access_token, access_secret)

    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=access_token,
                   resource_owner_secret=access_secret)
    return oauth


def get_user_authorization(request_token):
    """
    Redirect the user to authorize the client, and get them to give us the
    verification code.
    """
    authorize_url = AUTHORIZE_URL
    authorize_url = authorize_url.format(request_token=request_token)
    print 'Please go here and authorize:\n' + authorize_url
    return raw_input('Please input the verifier: ')


def get_access_token(request_token, request_secret, verifier):
    """"
    Get a token which will allow us to make requests to the API
    """
    oauth = OAuth1(CLIENT_KEY,
                   client_secret=CLIENT_SECRET,
                   resource_owner_key=request_token,
                   resource_owner_secret=request_secret,
                   verifier=verifier)

    response = requests.post(ACCESS_TOKEN_URL, auth=oauth)
    credentials = urlparse.parse_qs(response.content)
    access_token = credentials.get('oauth_token')[0]
    access_secret = credentials.get('oauth_token_secret')[0]
