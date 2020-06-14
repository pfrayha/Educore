from flask import Blueprint

performance = Blueprint('performance', __name__)

from . import views