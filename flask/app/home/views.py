from flask import render_template, redirect, url_for, abort, jsonify, json
from flask_login import login_required, current_user

from . import home
from .. import db
from ..models import User
import datetime

@home.route('/test')
def test():

	alunos = Pessoa.query.all()

	return render_template('home/test.html', alunos=alunos)

@home.route('/_test', methods=['GET', 'POST'])
def _test():
	alunos = Pessoa.query.all()
	print (json.dumps(Pessoa.serialize_list(alunos)))
	print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\n\n\n")
	return json.dumps(Pessoa.serialize_list(alunos))

@home.route('/')
def homepage():
    
    #Redirect pro login
    return redirect(url_for('auth.login'))

@home.route('/dashboard')
def dashboard():

	return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
def admin_dashboard():

	if not current_user.user_type.type_name == 'admin':
		abort(403)

	return render_template('home/admin_dashboard.html', title="Admin Dashboard")


# @home.route('/painel')
# @login_required
# def painel():

# 	# calcular datas
# 	hoje = datetime.datetime.today()
# 	segunda = (hoje - datetime.timedelta(days=hoje.weekday())).date()
# 	terca = (segunda + datetime.timedelta(days=1))
# 	quarta = (segunda + datetime.timedelta(days=2))
# 	quinta = (segunda + datetime.timedelta(days=3))
# 	sexta = (segunda + datetime.timedelta(days=4))
# 	sabado = (segunda + datetime.timedelta(days=5))
# 	domingo = (segunda + datetime.timedelta(days=6))

# 	# querys das atividades Neam
# 	atividades_neam_segunda = db.session.query(AtividadeNeam.pk_nome_atividade_neam, AtividadeNeam.hora_ini, AtividadeNeam.dia_semana).filter(AtividadeNeam.dia_semana == 'Segunda-Feira')
# 	atividades_neam_terca = db.session.query(AtividadeNeam.pk_nome_atividade_neam, AtividadeNeam.hora_ini, AtividadeNeam.dia_semana).filter(AtividadeNeam.dia_semana == 'Terça-Feira')
# 	atividades_neam_quarta = db.session.query(AtividadeNeam.pk_nome_atividade_neam, AtividadeNeam.hora_ini, AtividadeNeam.dia_semana).filter(AtividadeNeam.dia_semana == 'Quarta-Feira')
# 	atividades_neam_quinta = db.session.query(AtividadeNeam.pk_nome_atividade_neam, AtividadeNeam.hora_ini, AtividadeNeam.dia_semana).filter(AtividadeNeam.dia_semana == 'Quinta-Feira')
# 	atividades_neam_sexta = db.session.query(AtividadeNeam.pk_nome_atividade_neam, AtividadeNeam.hora_ini, AtividadeNeam.dia_semana).filter(AtividadeNeam.dia_semana == 'Sexta-Feira')
# 	atividades_neam_sabado = db.session.query(AtividadeNeam.pk_nome_atividade_neam, AtividadeNeam.hora_ini, AtividadeNeam.dia_semana).filter(AtividadeNeam.dia_semana == 'Sábado')
# 	atividades_neam_domingo = db.session.query(AtividadeNeam.pk_nome_atividade_neam, AtividadeNeam.hora_ini, AtividadeNeam.dia_semana).filter(AtividadeNeam.dia_semana == 'Domingo')
	
# 	# union das atividades neam e reforco
# 	atividades_segunda = atividades_neam_segunda.union(db.session.query(AulaReforco.pk_materia, AulaReforco.hora_ini, AulaReforco.pk_matricula_puc_pessoa).filter(AulaReforco.data == segunda )).order_by(AtividadeNeam.hora_ini).all()
# 	atividades_terca = atividades_neam_terca.union(db.session.query(AulaReforco.pk_materia, AulaReforco.hora_ini, AulaReforco.pk_matricula_puc_pessoa).filter(AulaReforco.data == terca )).order_by(AtividadeNeam.hora_ini).all()
# 	atividades_quarta = atividades_neam_quarta.union(db.session.query(AulaReforco.pk_materia, AulaReforco.hora_ini, AulaReforco.pk_matricula_puc_pessoa).filter(AulaReforco.data == quarta )).order_by(AtividadeNeam.hora_ini).all()
# 	atividades_quinta = atividades_neam_quinta.union(db.session.query(AulaReforco.pk_materia, AulaReforco.hora_ini, AulaReforco.pk_matricula_puc_pessoa).filter(AulaReforco.data == quinta )).order_by(AtividadeNeam.hora_ini).all()
# 	atividades_sexta = atividades_neam_sexta.union(db.session.query(AulaReforco.pk_materia, AulaReforco.hora_ini, AulaReforco.pk_matricula_puc_pessoa).filter(AulaReforco.data == sexta )).order_by(AtividadeNeam.hora_ini).all()
# 	atividades_sabado = atividades_neam_sabado.union(db.session.query(AulaReforco.pk_materia, AulaReforco.hora_ini, AulaReforco.pk_matricula_puc_pessoa).filter(AulaReforco.data == sabado )).order_by(AtividadeNeam.hora_ini).all()
# 	atividades_domingo = atividades_neam_domingo.union(db.session.query(AulaReforco.pk_materia, AulaReforco.hora_ini, AulaReforco.pk_matricula_puc_pessoa).filter(AulaReforco.data == domingo )).order_by(AtividadeNeam.hora_ini).all()

# 	# querys Eventos
# 	eventos_segunda = db.session.query(Evento.pk_nome, Evento.pk_data).filter(Evento.pk_data == segunda).all()
# 	eventos_terca = db.session.query(Evento.pk_nome, Evento.pk_data).filter(Evento.pk_data == terca).all()
# 	eventos_quarta = db.session.query(Evento.pk_nome, Evento.pk_data).filter(Evento.pk_data == quarta).all()
# 	eventos_quinta = db.session.query(Evento.pk_nome, Evento.pk_data).filter(Evento.pk_data == quinta).all()
# 	eventos_sexta = db.session.query(Evento.pk_nome, Evento.pk_data).filter(Evento.pk_data == sexta).all()
# 	eventos_sabado = db.session.query(Evento.pk_nome, Evento.pk_data).filter(Evento.pk_data == sabado).all()
# 	eventos_domingo = db.session.query(Evento.pk_nome, Evento.pk_data).filter(Evento.pk_data == domingo).all()

# 	lst_segunda = [atividades_segunda, eventos_segunda]
# 	lst_terca = [atividades_terca, eventos_terca]
# 	lst_quarta = [atividades_quarta, eventos_quarta]
# 	lst_quinta = [atividades_quinta, eventos_quinta]
# 	lst_sexta = [atividades_sexta, eventos_sexta]
# 	lst_sabado = [atividades_sabado, eventos_sabado]
# 	lst_domingo = [atividades_domingo, eventos_domingo]

# 	lst_semana = [lst_segunda, lst_terca, lst_quarta, lst_quinta, lst_sexta, lst_sabado, lst_domingo]
# 	str_dias = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
# 	str_datas = [segunda.strftime('%d/%m/%Y'), terca.strftime('%d/%m/%Y'), quarta.strftime('%d/%m/%Y'), quinta.strftime('%d/%m/%Y'), sexta.strftime('%d/%m/%Y'), sabado.strftime('%d/%m/%Y'), domingo.strftime('%d/%m/%Y')]

# 	limite_manha = datetime.time(12, 00)
# 	limite_tarde = datetime.time(18, 00)

# 	return render_template('home/painel_semana.html', limite_manha=limite_manha, limite_tarde=limite_tarde, str_datas=str_datas, str_dias=str_dias, lst_semana=lst_semana , title="Painel da Semana")