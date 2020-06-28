from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from . import performance
from ..manager_hub import ManagerHub

@performance.route('/report/generate_report/<string:report_type>', methods=['POST'])
@login_required
def generate_report(report_type):
	kwargs = request.args
	report_file = ManagerHub.get_hub_instance().report_manager.generate_report(report_type, **kwargs)
	return form