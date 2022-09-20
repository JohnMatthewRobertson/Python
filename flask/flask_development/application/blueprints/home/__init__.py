'''
 sets default
'''
from flask import Blueprint

blue_print = Blueprint('home', __name__, template_folder='templates')


from application.blueprints.home import routes
from application.blueprints.home.models import UserCar
