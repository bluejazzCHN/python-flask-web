from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config
from flask_login import LoginManager

bootsrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'userverify.login'


def app_create(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootsrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    from .main import blue 
    app.register_blueprint(blue)
    from .auth import userverify
    app.register_blueprint(userverify,url_prefix='/auth')
    
    return app
