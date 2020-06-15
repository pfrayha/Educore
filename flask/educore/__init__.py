from flask import Flask
from .manager_hub import ManagerHub

def configure_educore(app, registration_manager=None, performance_manager=None):
    ManagerHub.configure_hub_instance(registration_manager, performance_manager)

    from .people import people as people_blueprint
    app.register_blueprint(people_blueprint)

    from .performance import performance as performance_blueprint
    app.register_blueprint(performance_blueprint)

    return app