from ..manager_interfaces.report_manager import IReportManager

from flask import render_template

class ReportManager(IReportManager):
    @staticmethod
    def generate_report(student_id):
        
        return render_template("student/student.html")