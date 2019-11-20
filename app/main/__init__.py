from flask import Blueprint

blue = Blueprint(name='blue', import_name='blue')

from . import views, errors

