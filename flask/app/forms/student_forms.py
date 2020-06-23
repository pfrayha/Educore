from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, IntegerField, SelectField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from flask_wtf import FlaskForm
from wtforms_components import TimeField

class AddOrEditStudentForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    guardian_id = SelectField('Responsável', coerce=int)

    submit = SubmitField('Confirmar')
