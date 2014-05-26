#first import what is needed to support the code
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


# Then initialize the variables
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))


# Then import needed files already existing in the root folder

from app import models

# to import the user into our views and access the user, we must first
# define the user. We need the user model to make the user so this must come
# after importing models.
# models.User is used because User is in models.

user = db.session.query(models.User).filter_by(email='happy').first()
if user is None:
    user = models.User('Linda', 'lp', 'happy')
    db.session.add(user)
    db.session.commit()

food = db.session.query(models.Food).filter_by(name='kale').first()
if food is None:
    food = models.Food('kale', 1, 2, 3, 4)
    db.session.add(food)
    db.session.commit()

food = db.session.query(models.Food).filter_by(name='grapes').first()
if food is None:
    food = models.Food('grapes', 1, 2, 3, 4)
    db.session.add(food)
    db.session.commit()

db.session.close()

from app import views


