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

class UserType(db.Model):
    __tablename__ = 'user_types'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(128), unique=True, nullable=False)

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True, unique=True)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    user_type_id = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=False)
    user_type = db.relationship('UserType', backref=db.backref('users', lazy=True))

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

student_class_association = db.Table('student_classes',db.Model.metadata,
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
    db.Column('class_id', db.Integer, db.ForeignKey('classes.id'))
)
    
class Student(db.Model):
    __tablename__ = 'students'
    __table_args__ = (
        db.UniqueConstraint('name', 'guardian_id', name='unique_name_guardian'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    guardian_id = db.Column(db.Integer, db.ForeignKey('guardians.id'),nullable=False)
    classes = db.relationship('Class', secondary = student_class_association)

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(128), unique=True)

class Unit(db.Model):
    __tablename__ = 'units'

    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(128), unique=True)

class Class(db.Model):
    __tablename__ = 'classes'
    __table_args__ = (
        db.UniqueConstraint('subject_id', 'teacher_id', 'unit_id', name='unique_subject_teacher_unit'),
    )

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)

    subject = db.relationship('Subject', backref=db.backref('classes', lazy=True))
    teacher = db.relationship('User', backref=db.backref('classes', lazy=True))
    unit = db.relationship('Unit', backref=db.backref('classes', lazy=True))

    students = db.relationship('Student', secondary = student_class_association)

class Exam(db.Model):
    __tablename__ = 'exams'
    __table_args__ = (
        db.UniqueConstraint('exam_date', 'class_id', name='unique_exam_date_class'),
    )

    id = db.Column(db.Integer, primary_key=True)
    exam_date = db.Column(db.Date, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)

    exam_class = db.relationship('Class', backref=db.backref('exams', lazy=True))

class Grade(db.Model):
    __tablename__ = 'grades'
    __table_args__ = (
        db.UniqueConstraint('exam_id', 'student_id', name='unique_exam_student'),
    )

    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    grade = db.Column(db.Float(decimal_return_scale=2), nullable=False)

    exam = db.relationship('Exam', backref=db.backref('grades', lazy=True))
    student = db.relationship('Student', backref=db.backref('grades', lazy=True))

class Presence(db.Model):
    __tablename__ = 'presences'

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    presence_date = db.Column(db.Date, nullable=False)
    presence = db.Column(db.Boolean, nullable=False)
    
    presence_class = db.relationship('Class', backref=db.backref('presences', lazy=True))
    student = db.relationship('Student', backref=db.backref('presences', lazy=True))
