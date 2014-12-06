from app import app, db
from sqlalchemy import Column, Integer, String

class Car(db.Model):
    __tablename__='car'
    id          =   db.Column(Integer, primary_key=True)
    mfg         =   db.Column(String(200))
    model       =   db.Column(String(200))
    color       =   db.Column(String(200))
    year        =   db.Column(Integer)

    def __init__(self, mfg=None, model=None, color=None, year=None):
        self.mfg = mfg
        self.model = model
        self.color = color
        self.year = year


    def __repr(self):
        return "<Car {} {} {} {}>".format(self.mfg, self.model, self.color, self.year)
