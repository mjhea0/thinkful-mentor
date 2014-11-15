from sqlalchemy import Column, Integer, String, Sequence

from database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, Sequence('post_id_sequence'), primary_key=True)
    title = Column(String(128))
    body = Column(String(1024))

    def as_dictionary(self):
        post = {
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
        return post
