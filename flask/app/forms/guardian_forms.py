from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, IntegerField, SelectField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from flask_wtf import FlaskForm
from wtforms_components import TimeField

class AddOrEditGuardianForm(FlaskForm):
	name = StringField('Nome', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	cpf = StringField('CPF', validators=[DataRequired()])
	cellphone = StringField('Celular', validators=[DataRequired()]) 
	housephone = StringField('Telefone de Casa', validators=[Optional()])

	address_number = IntegerField('Número', validators=[DataRequired()])
	address_street = StringField('Rua', validators=[DataRequired()])
	address_complement = StringField('Complemento', validators=[Optional()])
	address_neighborhood = StringField('Bairro', validators=[DataRequired()])
	address_city = StringField('Cidade', validators=[DataRequired()])
	address_uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	address_cep = StringField('CEP', validators=[DataRequired()])
	
	submit = SubmitField('Confirmar')