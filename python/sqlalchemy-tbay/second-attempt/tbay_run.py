from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://localhost:5432/tbay3')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from tbay import Item, Bid


def get_high_bid(item_id):
    item = session.query(Item.name).filter(Item.id == item_id).first()
    high_bidder = session.query(Bid.bidder_id, Bid.price).\
        filter(Bid.item_id == item_id).\
        order_by(Bid.price.desc()).first()
    msg = "The winner of the '{0}' auction is {1} with a bid of {2}.".format(
        item[0], high_bidder[0], high_bidder[1])
    return msg


print get_high_bid(2)
