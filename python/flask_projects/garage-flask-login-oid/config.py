import os

SQLALCHEMY_DATABASE_URI= os.environ["DATABASE_URL"]
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = True
OPENID_PROVIDERS = {
    'google' : 'https://www.google.com/accounts/o8/id',
    'yahoo' : 'https://me.yahoo.com',
}
basedir = os.path.abspath(os.path.dirname(__file__))
