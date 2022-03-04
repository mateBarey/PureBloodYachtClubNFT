from flask import Blueprint, render_template

about = Blueprint('about',__name__,url_prefix='/about')

@about.route('/about')
def about():
    render_template('../templates/about/about.html')