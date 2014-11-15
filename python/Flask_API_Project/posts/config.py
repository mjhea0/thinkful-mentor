class DevelopmentConfig(object):
    DATABASE_URI = "sqlite:///posts-development.db"
    DEBUG = True


class TestingConfig(object):
    DATABASE_URI = "sqlite://"
    DEBUG = True
