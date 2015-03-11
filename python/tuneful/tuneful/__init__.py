import os

from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "tuneful.config.DevelopmentConfig")
app.config.from_object(config_path)

import api
import views

from database import Base, engine
Base.metadata.create_all(engine)
