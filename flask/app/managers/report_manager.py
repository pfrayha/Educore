from educore.manager_interfaces import IReportManager

from flask import render_template

class ReportManager(IReportManager):
    @staticmethod
    def generate_report(report_type, **kwargs):
        if report_type == 'performance_report' and 'student_id' in kwargs:
            
            return render_template("student/student.html")
        
        else: 
            return render_404