from sqlalchemy import Column, Integer, String
from app import db

class Message(db.Model):
    __tablename__='message'
    id  =   db.Column(db.Integer, primary_key=True)
    txt =   db.Column(db.String(200))

    def __init__(self, txt=None):
        self.txt = txt

    def __repr(self):
        return "<Message {}".format(self.txt)
