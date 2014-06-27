import os
from app import app, db


def runserver():
    port = 5000  # change port if needed
    app.run(host='0.0.0.0', debug=True, port=port)

if __name__ == '__main__':
    db.create_all()
    runserver()