'''
    create flask application
    register blueprints
'''
from flask import Flask, current_app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from mainConfiguration import developmentConfig

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()


def create_application_instance(configuration_class=developmentConfig):
    '''
        register
        database
        blueprints
        configuration
    '''

    application_instance = Flask(__name__)
    application_instance.config.from_object(configuration_class)

    from application.blueprints.home import blue_print as home_blue_print
    application_instance.register_blueprint(home_blue_print)

    db.init_app(application_instance)

    migrate.init_app(application_instance, db)

    bootstrap.init_app(application_instance)

    return application_instance
