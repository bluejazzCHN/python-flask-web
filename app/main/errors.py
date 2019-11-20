from flask import  render_template
from . import blue

@blue.app_errorhandler
def page_not_found(e):
    return render_template('404.html'),404

@blue.app_errorhandler
def internal_server_error(e):
    return render_template('500.html'),500