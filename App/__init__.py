from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from config import Config 
import os, config
from models import db
from .views.home import home


# create application instance
app = Flask(__name__)
app.config.from_object(Config)

app = Flask(__name__)
app.register_blueprint(home)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
