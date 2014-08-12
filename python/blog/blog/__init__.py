import os

from flask import Flask

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "blog.config.DevelopmentConfig")
app.config.from_object(config_path)

import views
import filters
import login