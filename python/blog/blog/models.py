import datetime

from sqlalchemy import Column, Integer, String, \
    Sequence, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine

from flask.ext.login import UserMixin


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, Sequence("post_id_sequence"), primary_key=True)
    title = Column(String(1024))
    content = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)
    author_id = Column(Integer, ForeignKey('users.id'))


"""
User model - inherits from Base class and Flask-Login's UserMixin class,
which adds a series of default methods which Flask-Login relies on to make
authentication work
"""


class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, Sequence("user_id_sequence"), primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))
    posts = relationship("Post", backref="author")


Base.metadata.create_all(engine)
