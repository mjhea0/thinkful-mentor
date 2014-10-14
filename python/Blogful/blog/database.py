"""
This file is used for setting up a connection to the database,
which will be used to store our blog posts
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from blog import app
"""
Basic boilerplate code for using SQLAlchemy to work with a database
"""
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
#create a declaritive_base, then start a new session
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
