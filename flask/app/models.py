from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.inspection import inspect
from sqlalchemy import LargeBinary, ARRAY, Column, Date, Enum, Float, ForeignKey, ForeignKeyConstraint, Integer, SmallInteger, String, Table, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
import datetime

from . import models

from app import db, login_manager