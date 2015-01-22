from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://localhost:5432/tbay3')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String)

    item = relationship('Item', backref='owner')
    bidder = relationship('Bid', backref='bidder')


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    auction_item = relationship('Bid', backref='auction_item')


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)

#bid_item_table = Table('bid_item_associaton', Base.metadata,
                      #Column('bid_id', Integer, ForeignKey('bids.id')),
                      #Column('item_id', Integer, ForeignKey('items.id'))
                      #)

Base.metadata.create_all(engine)
