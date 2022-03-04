from posixpath import abspath
from flask import Blueprint, render_template
import os 
home = Blueprint('home',__name__,url_prefix='/')

home_dir = os.path.abspath('./App/templates/home')
@home.route('/')
def index():
    print(home_dir)
    render_template(home_dir + '/index.html' )