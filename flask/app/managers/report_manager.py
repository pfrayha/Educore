
from educore.manager_interfaces import IReportManager

from flask import render_template, send_file
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

class ReportManager(IReportManager):
    @staticmethod
    def generate_report(report_type, **kwargs):
        if report_type == 'performance_report' and 'student_id' in kwargs:
            from ..models import Student
            from app import db
            import pdfkit

            student = db.session.query(Student).get_or_404(kwargs['student_id'])
            initial_date = datetime.strptime(kwargs['initial_date'][0],'%d-%m-%Y').date() if 'initial_date' in kwargs else (date.today() - relativedelta(months=3)).replace(day=1)
            final_date = datetime.strptime(kwargs['final_date'][0],'%d-%m-%Y').date() if 'final_date' in kwargs else date.today()

            table_size = max([len([exam for exam in x.exams if (exam.exam_date >= initial_date and exam.exam_date <= final_date)]) for x in student.classes])
            
            class_grades = {c: [grade.grade for grade in student.grades if (grade.exam.exam_class == c and grade.exam.exam_date >= initial_date and grade.exam.exam_date <= final_date)] for c in student.classes}
            grade_averages = {c: sum(grades)/len(grades) if len(grades) > 0 else 0 for c, grades in class_grades.items()}

            report_template = render_template("report/student_performance_report.html", student=student, table_size=table_size, class_grades=class_grades, grade_averages=grade_averages, initial_date=initial_date, final_date=final_date)

            options = {
                'encoding': "UTF-8"
            }

            pdfkit.from_string(report_template, '.\\temp.pdf', options=options)

            return send_file("..\\temp.pdf", mimetype='pdf', as_attachment=True, attachment_filename=f"Relatório_de_Performance_{student.name}.pdf")
        else: 
            return render_404