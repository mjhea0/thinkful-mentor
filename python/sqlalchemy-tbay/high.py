from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text


engine = create_engine('postgresql://localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def get_highest_bid():
    command = text(
        """
        SELECT price, username, item_id
        FROM bids JOIN users ON users.id=bids.bidder_id
        ORDER BY price DESC LIMIT 1
        """
    )

    result = engine.execute(command)
    return result


def get_user_name(user_id):
    command = text(
        """
        SELECT name FROM items WHERE id = %d
        """ % (user_id)
    )
    result = engine.execute(command)
    for value in result:
        return value[0]


values = []
for value in get_highest_bid():
    user_name = get_user_name(value[2])
    values.extend([value[0], value[1], user_name])

print "The winner of the '{2}' auction is {1} with a bid of {0}.".format(
    values[0], values[1], values[2])
