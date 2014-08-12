import os


class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-development.db"
    DEBUG = True
    SECRET_KEY = os.environ.get("BLOGFUL_SECRET_KEY", "")
