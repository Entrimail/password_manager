from . import db
from flask_login import UserMixin


class Note(db.Model):    
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(150))
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')


    
    
