from flask import Blueprint, render_template, request, redirect, url_for, flash

post = Blueprint('post', __name__)


@post.route('/posts')
def posts():
    return render_template('blog_21.html')