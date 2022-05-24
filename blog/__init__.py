from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fdsaknmnvuqroipcklam knfkla'  # encrypt the cookies and session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from blog.main.main import main
    from blog.user.user import user

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(user, url_prefix='/')

    from models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'user.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('blog/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
