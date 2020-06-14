from flask import flash, redirect, render_template, url_for
# from flask_login import login_required, login_user, logout_user, current_user
from . import performance
from ..manager_hub import ManagerHub

@performance.route('/performance/generate_report/<string:student_id>', methods=['POST'])
# @login_required
def generate_report(student_id):
	report_file = ManagerHub.get_hub_instance().report_manager.generate_report(student_id)
	return form