from app import app, db
from sqlalchemy import Column, Integer, String

class Car(db.Model):
    __tablename__='car'
    id          = db.Column(Integer, primary_key=True)
    mfg         = db.Column(String(200))
    model       = db.Column(String(200))
    color       = db.Column(String(200))
    year        = db.Column(Integer)
    owner_id    = db.Column(Integer, db.ForeignKey('user.id'))

    def __init__(self, mfg=None, model=None, color=None, year=None):
        self.mfg = mfg
        self.model = model
        self.color = color
        self.year = year

    def __repr__(self):
        return "<Car {} {} {} {}>".format(self.mfg, self.model, self.color, self.year)

class User(db.Model):
    __tablename__='user'
    id      = db.Column(Integer, primary_key=True)
    email   = db.Column(String(200))
    cars    = db.relationship("Car", backref="owner", lazy='dynamic')

    def __init__(self, email=None):
        self.email = email

    def __repr__(self):
        return "<User {}>".format(self.email)

    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False