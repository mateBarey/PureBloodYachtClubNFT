from posixpath import abspath
from flask import Blueprint, render_template
import os 
home = Blueprint('home',__name__,url_prefix='/')

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/about')
def about():
    return render_template('home/about.html')


@home.route('/register')
def register():
    return render_template('home/register.html')