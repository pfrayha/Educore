from flask import Flask
from .manager_hub import ManagerHub

def configure_educore(app, people_manager=None, report_manager=None):
    ManagerHub.configure_hub_instance(people_manager, report_manager)

    from .people import people as people_blueprint
    app.register_blueprint(people_blueprint)

    from .report import report as report_blueprint
    app.register_blueprint(report_blueprint)

    return app