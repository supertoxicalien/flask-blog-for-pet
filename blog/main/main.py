from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user
from blog.user.forms import LoginForm
from models import User
from werkzeug.security import generate_password_hash, check_password_hash


main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index_page():
    return render_template('index_2.html')


@main.route('/about')
def about_page():
    return render_template('about_2.html')


@main.route('/test', methods=['GET', 'POST'])
def test():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('main.index_page'))
        else:
            flash('Error. Try again', category='error')
            return redirect(url_for('main.test'))

    return render_template('log.html', form=form)
