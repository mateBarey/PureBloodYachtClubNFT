from flask import Blueprint, render_template

register = Blueprint('about',__name__,url_prefix='/register')

@register.route('/')
def about():
    return render_template('register/register.html')