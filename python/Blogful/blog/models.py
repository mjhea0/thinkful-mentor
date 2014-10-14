"""
Create a SQLAlchemy model, which will be used to store and retrieve blog posts
"""

import datetime

from sqlalchemy import Column, Integer, String, Sequence, Text, DateTime

from database import Base, engine


#create a new class, which inherits from the declaritive base object
class Post(Base):
    #give model a table name
    __tablename__ = "posts"

    #primary key id column
    id = Column(Integer, Sequence("post_id_sequence"), primary_key=True)
    #column for title of the post
    title = Column(String(1024))
    #column for the content of the post
    content = Column(Text)
    #date and time the post was created
    datetime = Column(DateTime, default=datetime.datetime.now)

#use the following function to create the table in the database
Base.metadata.create_all(engine)
