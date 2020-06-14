from flask import Flask
from .manager_hub import ManagerHub
from .managers.registration_manager import RegistrationManager

def create_app(config_name=''):
    app = Flask(__name__)

    ManagerHub.configure_hub_instance(RegistrationManager)

    from .student import student as student_blueprint
    app.register_blueprint(student_blueprint)

    return app