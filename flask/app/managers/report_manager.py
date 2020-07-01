
from educore.manager_interfaces import IReportManager

from flask import render_template

class ReportManager(IReportManager):
    @staticmethod
    def generate_report(report_type, **kwargs):
        if report_type == 'performance_report' and 'student_id' in kwargs:
            from ..models import Student
            from app import db
            import pdfkit
            from io import BytesIO

            student = db.session.query(Student).get_or_404(kwargs['student_id'])
            table_size = max([len(x.exams) for x in student.classes])
            
            class_grades = {c: [grade.grade for grade in student.grades if grade.exam.exam_class == c] for c in student.classes}
            grade_averages = {c: sum(grades)/len(grades) if len(grades) > 0 else 0 for c, grades in class_grades.items()}

            report_template = render_template("report/student_performance_report.html", student=student, table_size=table_size, class_grades=class_grades, grade_averages=grade_averages)

            return report_template
        else: 
            return render_404