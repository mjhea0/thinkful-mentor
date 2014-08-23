class DevelopmentConfig(object):
    DATABASE_URI = "sqlite:///yum-dev.db"
    DEBUG = True


class TestingConfig(object):
    DATABASE_URI = "sqlite://yum-test.db"
    DEBUG = True
