from wtforms import PasswordField, StringField, SubmitField, ValidationError, BooleanField, IntegerField, SelectField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from flask_wtf import FlaskForm
from wtforms_components import TimeField

class AddOrEditAlunoAprendizForm(FlaskForm):

	"""
	Form para adição/edição de um aluno/aprendiz
	"""

	nome = StringField('Nome', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	foto = FileField('Foto', validators=[Optional()])
	sexo = SelectField('Sexo', choices=[('M','Masculino'), ('F','Feminino'), ('O', 'Outro')])
	data_nascimento = DateField('Data de nascimento', format='%Y-%m-%d', validators=[DataRequired(message="Data inválida.")])
	data_ingresso = DateField('Data de Ingresso', format='%Y-%m-%d', validators=[DataRequired()])
	desligamento_data = DateField('Data de Desligamento', format='%Y-%m-%d', validators=[Optional()])
	desligamento_motivo = StringField('Motivo de Desligamento', validators=[Optional()])
	desligamento_destino = StringField('Destino', validators=[Optional()])
	identificador_tipo = SelectField('Tipo do identificador', choices=[('CPF','CPF'),('RG','RG'),('Certidão','Certidão de nascimento')], validators=[DataRequired()])	
	identificador_numero = StringField('Número do identificador', validators=[DataRequired()])
	identificador_complemento = SelectField('Complemento do identificador', choices=[('','Nenhum'),('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[Optional()])
	endereco_numero = IntegerField('Número', validators=[DataRequired()])
	endereco_rua = StringField('Rua', validators=[DataRequired()])
	endereco_complemento = StringField('Complemento', validators=[Optional()])
	endereco_bairro = StringField('Bairro', validators=[DataRequired()])
	endereco_cidade = StringField('Cidade', validators=[DataRequired()])
	endereco_uf = SelectField('UF', choices=[('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'), ('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'), ('MG','MG'), ('PA','PA'), ('PB','PB'), ('PR','PR'), ('PE','PE'), ('PI','PI'), ('RJ','RJ'), ('RN','RN'), ('RS','RS'), ('RO','RO'), ('RR','RR'), ('SC','SC'), ('SP','SP'), ('SE','SE'), ('TO', 'TO')], validators=[DataRequired()])
	endereco_cep = StringField('CEP', validators=[DataRequired()])
	nome_responsavel = StringField('Nome do responsável', validators=[Optional()])
	telefone_responsavel = StringField('Telefone do responsável', validators=[Optional()])
	profissao_responsavel = StringField('Profissão do responsável', validators=[Optional()])
	dificuldade = StringField('Dificuldade do aluno', validators=[Optional()])
	serie = SelectField('Série/Ano', choices=[('1o ano','1o ano'), ('2o ano','2o ano'), ('3o ano','3o ano'), ('4o ano','4o ano'), ('5o ano','5o ano'), ('6o ano','6o ano'), ('7o ano','7o ano'), ('8o ano','8o ano'), ('9o ano','9o ano') ], validators=[Optional()])
	escolaridade_nivel = SelectField('Nível de escolaridade', choices=[('Fundamental Completo','Fundamental Completo'), ('Fundamental Incompleto','Fundamental Incompleto'), ('Médio Completo','Médio Completo'), ('Médio Incompleto','Médio Incompleto'), ('Técnico Completo', 'Técnico Completo'), ('Técnico Incompleto', 'Técnico Incompleto')], validators=[Optional()])
	escolaridade_turno = SelectField('Turno', choices=[('Manha','Manhã'), ('Tarde','Tarde'), ('Noite','Noite')], validators=[Optional()])
	nome_instituicao = StringField('Nome da instituição de origem', validators=[Optional()])

	submit = SubmitField('Confirmar')


class AddOrEditVoluntarioForm(FlaskForm):

	"""
	Form para adição/edição de um voluntario
	"""

	nome = StringField('Nome', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	celular = IntegerField('Celular', validators=[DataRequired()])
	foto = FileField('Foto', validators=[Optional()])
	sexo = SelectField('Sexo', choices=[('M','Masculino'), ('F','Feminino'), ('O', 'Outro')])
	data_ingresso = DateField('Data de Ingresso', format='%Y-%m-%d', validators=[DataRequired()])
	desligamento_data = DateField('Data de Desligamento', format='%Y-%m-%d', validators=[Optional()])
	desligamento_motivo = StringField('Motivo de Desligamento', validators=[Optional()])
	curso_puc = StringField('Curso na PUC', validators=[Optional()])
	matricula_puc = StringField('Matrícula na PUC', validators=[Optional()])

	
	submit = SubmitField('Confirmar')