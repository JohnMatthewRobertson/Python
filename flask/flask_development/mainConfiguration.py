'''
    configuration settings
    loads from environment file
'''
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class developmentConfig(object):
    """LOAD ENVIRONMENT variables from .env"""

    SECRET_KEY = os.environ.get('SOMETHING_REALLY_HARD_TO_GUESS_SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TESTING = True

    DEBUG = True

