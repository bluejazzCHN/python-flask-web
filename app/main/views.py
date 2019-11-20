from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import blue
from .forms import NameForm
from app import db
from ..models import User
from flask_login import login_required


@blue.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
            flash('Looks like you have changed your name!')

        session['name'] = form.name.data
        form.name.data = ''
        redirect(url_for('.index'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False))


@blue.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
