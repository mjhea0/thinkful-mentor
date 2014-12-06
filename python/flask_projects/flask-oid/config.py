import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.environ["SECRET_KEY"]
OPENID_PROVIDERS = {
    'google' : 'https://www.google.com/accounts/o8/id',
    'yahoo' : 'https://me.yahoo.com',
    'myOpenId': 'https://www.myopenid.com'
}