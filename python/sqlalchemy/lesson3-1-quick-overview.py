from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "Species: %s" % self.name

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()

Base.metadata.create_all(engine)

cat = Species(name="Cat")     
dog = Species(name="Dog")
db_session.add(cat)
db_session.add(dog)
# alternatively db_session.add_all([cat, dog])
db_session.commit()

pets = db_session.query(Species).all()
for pet in pets:
  print "Id: {}, Name: {}".format(pet.id, pet.name)

db_session.close()