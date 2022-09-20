'''
    model for user
'''
from application import db


class UserCar(db.Model):
    '''
        user class details
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    car = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f'{self.name} {self.car}'