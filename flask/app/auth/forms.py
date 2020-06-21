from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf import FlaskForm

from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Nome Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password_confirmation = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    user_type_id = SelectField('Tipo de Usuário', coerce=int)
    enabled = BooleanField('Habilitado')
    submit = SubmitField('Registrar')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email já em uso.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Nome de usuário já em uso.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')
