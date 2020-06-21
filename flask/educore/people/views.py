from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user
from . import people
from ..manager_hub import ManagerHub

@people.route('/people/new_guardian', methods=['GET'])
@login_required
def new_guardian():
	form = ManagerHub.get_hub_instance().registration_manager.get_registration_form(model='guardian')
	return form

@people.route('/people/new_guardian', methods=['POST'])
@login_required
def submit_guardian_form():
	response = ManagerHub.get_hub_instance().registration_manager.submit_registration_form(model='guardian')

@people.route('/people/new_volunteer', methods=['GET'])
@login_required
def new_volunteer():
	form = ManagerHub.get_hub_instance().registration_manager.get_registration_form(model='volunteer')
	return form

@people.route('/people/new_student', methods=['GET'])
@login_required
def new_student():
	form = ManagerHub.get_hub_instance().registration_manager.get_registration_form(model='student')
	return form