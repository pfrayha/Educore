from educore.manager_interfaces import IRegistrationManager

from flask import render_template
from ..forms.guardian_forms import AddOrEditGuardianForm
from ..forms.student_forms import AddOrEditStudentForm

# from ..models import Guardian, Student

class RegistrationManager(IRegistrationManager):
    @staticmethod
    def get_registration_form(model):
        if model == 'guardian':
            form = AddOrEditGuardianForm()
            template = 'people/add_or_edit_guardian.html'
        elif model == 'student':
            from ..models import Guardian
            form = AddOrEditStudentForm()
            form.guardian_id.choices = [(t.id, t.type_name) for t in Guardian.query.order_by("name")]
            template = 'people/add_or_edit_student.html'
        return render_template(template, form=form)

    @staticmethod
    def submit_registration_form(model):
        pass