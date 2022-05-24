from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index_page():
    return render_template('index_2.html')


@main.route('/about')
def about_page():
    return render_template('about_2.html')