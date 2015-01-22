from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://localhost:5432/tbay3')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from tbay import User, Item, Bid

kyle = User(username='kyle')
zach = User(username='zachary')
leigh = User(username='leigh')

session.add_all([kyle, zach, leigh])
session.commit()

baseball = Item(name='mlb baseball', owner=kyle)
football = Item(name='nfl football', owner=zach)
piano = Item(name='grand piano', owner=leigh)

session.add_all([baseball, football, piano])
session.commit()

bid01 = Bid(price=17.50, bidder=kyle, auction_item=football)
bid02 = Bid(price=5175, bidder=zach, auction_item=piano)
bid03 = Bid(price=21.25, bidder=leigh, auction_item=football)
bid04 = Bid(price=18.75, bidder=zach, auction_item=football)
bid05 = Bid(price=27.00, bidder=kyle, auction_item=football)
bid06 = Bid(price=5500, bidder=kyle, auction_item=piano)

session.add_all([bid01, bid02, bid03, bid04, bid05, bid06])
session.commit()
