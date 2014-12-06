from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, Text, Table
from sqlalchemy.orm import relationship, backref

from sqlalchemy.orm import sessionmaker
 
import logging
log = logging.getLogger(__name__)

################################################################################
# set up logging - see: https://docs.python.org/2/howto/logging.html

# when we get to using Flask, this will all be done for us
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
log.addHandler(console_handler)


################################################################################
# Domain Model

Base = declarative_base()
log.info("base class generated: {}".format(Base) )

# define our domain model
class Species(Base):
    """
    domain model class for a Species
    """
    __tablename__ = 'species'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breeds = relationship('Breed', backref="species", cascade="all, delete-orphan")

    # methods
    def __repr__(self):
        return self.name                   


class Breed(Base):
    """
    domain model class for a Breed
    has a with many-to-one relationship Species
    """
    __tablename__ = 'breed'

    # database fields
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False) 
    pets = relationship('Pet', backref='breed')

    # there's a back ref on species that let's you get from breed to species

    def __repr__(self):
        return "{}: {}".format(self.name, self.species) 


class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    website = Column(Text, nullable=False)
    pets = relationship('Pet', backref="shelter")

    def __repr__(self):
            return self.name

# our many-to-many association table, in our model *before* Pet class 
pet_person_table = Table('pet_person', Base.metadata,
    Column('pet_id', Integer, ForeignKey('pet.id'), nullable=False),
    Column('person_id', Integer, ForeignKey('person.id'), nullable=False)
)


class Pet(Base):
    __tablename__ = 'pet'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    breed_id = Column(Integer, ForeignKey('breed.id')) 
    shelter_id = Column(Integer, ForeignKey('shelter.id')) 

    # must be nullable, as some pets will be the roots of our trees!
    parent_id = Column(Integer, ForeignKey(id), nullable=True ) 
    children = relationship('Pet', backref=backref('parent', remote_side=id) )

    # mapped "owners" relationship on backref in Person
    
    def __repr__(self):
        return self.name       


class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    city = Column(String)
    email = Column(String)
    
    # mapped relationship, pet_person table must already be in scope!
    pets = relationship('Pet', secondary=pet_person_table, backref='owners')
    
    def __repr__(self):
        return self.name

################################################################################
def init_db(engine):
    "initialize our database, drops and creates our tables"
    log.info("init_db() engine: {}".format(engine) )
    
    # drop all tables and recreate
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    log.info("  - tables dropped and created")



if True:
    log.info("main executing:")              

    # create an engine
    engine = create_engine('sqlite:///test.db')
    log.info("created engine: {}".format(engine) )
    init_db(engine)

    # call the sessionmaker factory to make a Session class 
    Session = sessionmaker(bind=engine)
    
    # get a local session for the this script
    db_session = Session()
    log.info("Session created: {}".format(db_session) )


    # seed our database!
    log.info("Seeding database")   
    cat = Species(name="cat")
    dog = Species(name="dog")
    birman = Breed(name="Birman", species=cat)
    tabby = Breed(name="Tabby", species=cat)
    american_curl = Breed(name="American Curl", species=cat)
    golden = Breed(name="Golden Retriever", species=dog)
    dalmatian = Breed(name="Dalmatian", species=dog)
    poodle = Breed(name="Poodle", species=dog)
    mixed = Breed(name="mixed", species=dog)

    nyc_shelter = Shelter(name="New York Home for Orphaned Animals", 
        website="http://www.nyhfoa.org")
    cincinatti_shelter = Shelter(name="Cincinatti Pet Hotel", 
        website="http://www.cph.org")


    garfield_1 = Pet(name="Garfield", breed=tabby)
    garfield_2 = Pet(name="Garfield", breed=tabby, parent=garfield_1)
    spot = Pet(name="Spot", breed=dalmatian)
    spot_jr = Pet(name="Spot Junior", breed=dalmatian,
        shelter=cincinatti_shelter, parent=spot)
    spot_3 = Pet(name="Spot the Third", parent=spot_jr, breed=mixed)
    molly = Pet(name="Molly", breed=golden, shelter=nyc_shelter)
    tom = Person(name="Tom", pets=[spot_jr, spot, garfield_1],
        email="tom@gmail.com", city="New York")
    ruth = Person(name="Ruth", pets=[spot_jr, spot, spot_3, garfield_2])

    # import pdb
    # pdb.set_trace()

    db_session.add_all([birman, tabby, american_curl, golden, dalmatian,
        poodle, nyc_shelter, cincinatti_shelter, spot_jr, molly, tom, ruth,
        garfield_1, garfield_2, spot_3])
    db_session.commit()
    # db_session.close()
    # log.info("all done!")
