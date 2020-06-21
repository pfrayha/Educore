from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.inspection import inspect
from sqlalchemy import LargeBinary, ARRAY, Column, Date, Enum, Float, ForeignKey, ForeignKeyConstraint, Integer, SmallInteger, String, Table, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
import datetime

from . import models

from app import db, login_manager

Base = declarative_base()

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True, unique=True)
    clearance = db.Column(db.Integer, nullable=False, default=0)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<email {}>'.format(self.email)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Guardian(db.Model):
    __tablename__ = 'guardians'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    cpf = db.Column(db.String(15), unique=True, )
    cellphone = db.Column(db.String(15))
    housephone = db.Column(db.String(15))

    address_number = db.Column(db.SmallInteger)
    address_street = db.Column(db.String(100))
    address_complement = db.Column(db.String(50))
    address_neighborhood = db.Column(db.String(20))
    address_city = db.Column(db.String(20))
    address_uf = db.Column(db.CHAR(2))
    address_cep = db.Column(db.CHAR(8))

    dependants = db.relationship('Student',backref=db.backref('guardian', lazy=True))
    
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    guardian_id = db.Column(db.Integer, db.ForeignKey('guardians.id'),nullable=False)