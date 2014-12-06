from flask import Flask
from flask.ext.openid import OpenID
from config import basedir
import os 

app = Flask(__name__)
app.config.from_object("config")
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views