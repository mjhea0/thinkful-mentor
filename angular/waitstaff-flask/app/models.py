from app import db


class Earning(db.Model):

    __tablename__ = 'earnings'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    tax_rate = db.Column(db.Integer)
    tip_rate = db.Column(db.Integer)

    def __init__(self, price, tax_rate, tip_rate):
        self.price = price
        self.tax_rate = tax_rate
        self.tip_rate = tip_rate