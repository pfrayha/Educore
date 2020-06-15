from educore.manager_interfaces import IRegistrationManager

from flask import render_template

class RegistrationManager(IRegistrationManager):
    @staticmethod
    def get_registration_form(model):
        return render_template("student/student.html")

    @staticmethod
    def submit_registration_form(json_data):
        pass