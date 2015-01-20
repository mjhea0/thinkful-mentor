from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text


engine = create_engine('postgresql://localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def get_highest_bid():
    command = text("""
        SELECT price, username
        FROM bids JOIN users ON users.id=bids.bidder_id
        ORDER BY price DESC LIMIT 1
        """)

    result = engine.execute(command)
    return result

values = []
for value in get_highest_bid():
    values.extend([value[0], value[1]])
print "The winner is {1} with a bid of {0}.".format(values[0], values[1])

list_comp = [value for valuesk in get_highest_bid()]
print "The winner is {1} with a bid of {0}.".format(
    list_comp[0][0], list_comp[0][1])
