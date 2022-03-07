from flask import Blueprint, render_template,flash,redirect, url_for, session
import os 
from flask import jsonify, request
from database import db, users
import bcrypt  
from forms import MyForm


from pymongo import MongoClient
from config import Config 

client = MongoClient(Config.MONGO_DATABASE_URI)
db = client.SimlarityDB

users = db["Users"]
home = Blueprint('home',__name__,url_prefix='/')


def alreadyRegistered(email):
    if users.find({"email":email}).count()== 0:
        return False
    else :
        return True 

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/about')
def about():
    return render_template('home/about.html')



@home.route('/register', methods = ['Get','POST'])
def register():
    if request.method == 'GET':
        return render_template('home/register.html')
    
    else:
        #postedData = request.get_json()
        email = request.form.get("email")
        username = email.split('@')[0]
        eth_address = request.form.get("eth_address")
        print(eth_address)
        password = request.form.get("password")
        print(password)
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        if alreadyRegistered(email) == True:
            retJson = {
                "status": 301,
                "msg": "User Already registered!"
            }
            return jsonify(retJson)
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        users.insert({
            "username": username,
            "email": email,
            "pasword": password,
            "eth_address": eth_address
        })
        return redirect(url_for('home.index'))

    


@home.route('/roadmap')
def map():
    return render_template('home/map.html')