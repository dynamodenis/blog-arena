from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy


#intialize extentions
db=SQLAlchemy()

def create_app(config_name):

    app=Flask(__name__)

    #REGISTER EXTENTIONS
    db.init_app(app)
    #REGISTER BLUEPRINTS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')


    #REGISTER CONFIGURASTION
    app.config.from_object(config_options[config_name])


    return app