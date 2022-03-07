from flask import Flask
from config import Config 
import os, config
from views.home import home
import datetime
from datetime import *
# create application instance


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(home)


if __name__ =='__main__':
    app.run(host='0.0.0.0')
