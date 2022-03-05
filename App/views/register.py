from flask import Blueprint, render_template

register = Blueprint('register',__name__,url_prefix='/register')

@register.route('/')
def register():
    return render_template('register/register.html')