from flask import flash, redirect, render_template, url_for
# from flask_login import login_required, login_user, logout_user, current_user
from . import student
from ..manager_hub import ManagerHub

@student.route('/student/home')
# @login_required
def students():
	form = ManagerHub.get_hub_instance().registration_manager.get_registration_form()
	return form