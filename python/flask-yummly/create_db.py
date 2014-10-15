from yummly import db
from yummly.models import User

db.create_all()

# insert data
db.session.add(User("admin", "ad@min.com", "admin"))


# commit the changes
db.session.commit()
