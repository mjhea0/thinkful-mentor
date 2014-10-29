from yummly import db
from yummly.models import User

db.create_all()

# insert data
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.commit()

# sanity check!
admin = User.query.filter_by(name='admin').first()
print admin.name
