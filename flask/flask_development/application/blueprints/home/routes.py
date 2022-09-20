'''
    url endpoints for home page
'''
from flask import render_template, request, current_app
from application.blueprints.home import blue_print
from application.blueprints.home.forms import  AddUserCar
from application.blueprints.home.models import UserCar
from application import db


@blue_print.route('/', methods=['GET', 'POST'])
@blue_print.route('/index', methods=['GET', 'POST'])
def index():
    '''
        hanldes GET and POST request
        for http://localhost:5000/
    '''

    if request.method == 'POST':
        user = UserCar(name=request.form.get('name'), car=request.form.get('car'))
        db.session.add(user)
        db.session.commit()

    form = AddUserCar()
    user_car = UserCar.query.all()

    return render_template('index.html',
                           title='Home',
                           detail=user_car,
                           form=form)
