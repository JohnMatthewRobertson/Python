'''
 form for entering data
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddUserCar(FlaskForm):
    '''
        example fields and settings
    '''
    name = StringField('Name', validators=[DataRequired()])
    car = StringField('Car', validators=[DataRequired()])
    submit = SubmitField('Submit')
