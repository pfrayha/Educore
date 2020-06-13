from flask import flash, redirect, render_template, url_for
# from flask_login import login_required, login_user, logout_user, current_user
from . import student

@student.route('/student/home')
# @login_required
def students():

    return render_template('student/student.html')

	# if not current_user.permissao == 0:
		# abort(403)

	# usuarios = Usuario.query.filter_by(permissao=0).all()


	# return render_template('admin/aprovar_usuarios.html', title="Admin Dashboard", usuarios=usuarios)