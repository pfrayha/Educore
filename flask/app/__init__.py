from flask import Flask

def create_app(config_name=''):
    app = Flask(__name__)

    from .student import student as student_blueprint
    app.register_blueprint(student_blueprint)

    return app