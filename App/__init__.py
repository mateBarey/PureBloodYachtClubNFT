from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config 
import os, config
from models import db
from views.home import home
from views.register import register
# create application instance


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(home)

Migrate(app, db)


if __name__ =='__main__':
    app.run(host='0.0.0.0')