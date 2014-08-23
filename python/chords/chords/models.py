import os.path

from flask import url_for
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from chords import app
from chords.utils import upload_path
from database import Base, engine, session

class Song(Base):
    __tablename__ = "Song"

    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('File.id'), nullable=False)

    def as_dictionary(self):
        file = session.query(File).filter_by(id=self.file_id).first()
        Song.as_dictionary = {
            "id": self.id, 
            "file": {
                "id": file.id, 
                "name": file.filename
        }       
        }
        return Song.as_dictionary

class File(Base):
    __tablename__ = "File"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    song = relationship("Song", backref="File")

    def as_dictionary(self):
        File.as_dictionary = {
            "id": self.id,
            "name": self.filename,
        }
        return File.as_dictionary
Base.metadata.create_all(engine)