from flask import Flask
from educore import configure_educore
from .managers.registration_manager import RegistrationManager
from .managers.report_manager import ReportManager  

def create_app(config_name=''):
    app = Flask(__name__)

    app = configure_educore(app, RegistrationManager, ReportManager)

    return app
