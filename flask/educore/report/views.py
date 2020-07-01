from flask import flash, redirect, render_template, url_for, request, send_file
from flask_login import login_required, login_user, logout_user, current_user
from . import report
from ..manager_hub import ManagerHub

@report.route('/report/generate_report/<string:report_type>', methods=['GET','POST'])
@login_required
def generate_report(report_type):
	args = request.args
	return ManagerHub.get_hub_instance().report_manager.generate_report(report_type, **args)