from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap  import Bootstrap


#intialize extentions
db=SQLAlchemy()
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.session_protection='Strong'
login_manager.login_view='auth.login'

def create_app(config_name):

    app=Flask(__name__)

    #REGISTER EXTENTIONS
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    #REGISTER BLUEPRINTS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')


    #REGISTER CONFIGURASTION
    app.config.from_object(config_options[config_name])

    from .models import create_configuration
    create_configuration(app)


    return app