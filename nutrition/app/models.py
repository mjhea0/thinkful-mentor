from itertools import chain
from sqlalchemy import create_engine, Column, \
Integer, String, Float, ForeignKey, Table, ForeignKeyConstraint
from sqlalchemy import Sequence
from sqlalchemy.ext.associationproxy  import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from app import db
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


#consider renaming association_table to something more description and as plurals
class Association(db.Model):
    __tablename__ = 'association'
    id = db.Column(db.Integer, db.Sequence('association_id_seq'), primary_key=True)
    food_log_id = db.Column(db.Integer, db.ForeignKey('food_logs.id'))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))
    quantity = db.Column(db.Float)
    #extra_data = Column(String(50))
    food = db.relationship('Food', backref='foodlog_assocs')

# This code is replaced by the class definition above.
#association_table = db.Table('association', db.Model.metadata,
    #db.Column('foods_id', db.Integer, db.ForeignKey('foods.id')),
    #db.Column('food_logs_id', db.Integer, db.ForeignKey('food_logs.id')),
    #)

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    name = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(12))
    email = db.Column(db.String(102), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    db.calorie_goal = db.Column(db.Integer)
    db.protein_goal = db.Column(db.Integer)
    db.carbohydrate_goal = db.Column(db.Integer)
    db.fat_goal = db.Column(db.Integer)
    db.weight = db.Column(db.Integer)
    
    #one to many
    food_logs = db.relationship('FoodLog', backref='user', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.password, self.email)

class Food(db.Model):#lists the nutrients.
    __tablename__ = 'foods'
    id = db.Column(db.Integer, db.Sequence('foods_id_seq'), primary_key=True)
    name = db.Column(db.String(50))
    calorie = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    carbohydrate = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    #food_log_id = Column(Integer, ForeignKey('food_log.id'))
    #backref does not meant the tablename. 
    #backref is a name to refer back to the original connection.

    
    
    def __init__(self, name, calorie, protein, carbohydrate, fat):
        self.name = name
        self.calorie = calorie
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

    def __repr__(self):
        return "<Food('%s','%d', '%d', '%d', '%d')>" % (self.name, 
            self.calorie, self.protein, self.carbohydrate, self.fat)

class FoodLog(db.Model):#continue using users as a model
#FoodLog is a list of foods eaten and the quantity eaten.
#be sure to read building a realtionship in the tutorial. Need to consider ForeignKey
#many to one is for the relationship between FoodLog and User
#a user can have multiple food_logs but food_log can have one users
#many to many is for relationship between FoodLog and Food
    __tablename__ = 'food_logs'
    id = db.Column(db.Integer, db.Sequence('food_logs_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))#many food_logs to one user
    #timestamp = db.Column(db.DateTime)

    #foods is being modified to be difined via the Association Object.
    #foods = db.relationship('Food', secondary=association_table, backref='food_logs')#many to many relationship
    #food_log may have many foods
    foods = db.relationship('Association')
        
    #instantiation not needed when used with SQLAlchemy.
    #AQLAlchemy automatically gives the __init__ constructor.
    #def __init__(self, name, quantity):
        #self.food_name = name
        #self.quantity = quantity
        
    #def __repr__(self):
        #return "<FoodLog('%s','%d')>" % (self.food_name, self.quantity)

db.create_all()


