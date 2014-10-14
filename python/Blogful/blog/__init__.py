import os

#import the Flask object
from flask import Flask

#create the app in the usual way
app = Flask(__name__)

config_path = os.environ.get("CONFIG_PATH", "blog.config.DevelopmentConfig")

app.config.from_object(config_path)


import views
import filters
