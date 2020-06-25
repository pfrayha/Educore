from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from . import people
from ..manager_hub import ManagerHub

@people.route('/people/new_<string:model>', methods=['GET', 'POST'])
@login_required
def new_person(model):
	if request.method == 'GET':
		form = ManagerHub.get_hub_instance().people_manager.get_registration_form(model)
		return form
	else:
		next_page = ManagerHub.get_hub_instance().people_manager.submit_registration_form(model)
		return next_page

@people.route('/people/edit_<string:model>/<int:id>', methods=['GET','POST'])
@login_required
def edit_person(model, id):
	if request.method == 'GET':
		form = ManagerHub.get_hub_instance().people_manager.get_registration_form(model, id)
		return form
	else:
		next_page = ManagerHub.get_hub_instance().people_manager.submit_registration_form(model, id)
		return next_page

@people.route('/people/list_<string:model>', methods=['GET'])
@login_required
def list_people(model):
	form = ManagerHub.get_hub_instance().people_manager.get_registration_form(model)
	return form