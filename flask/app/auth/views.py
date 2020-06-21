from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User, UserType

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    form.user_type_id.choices = [(t.id, t.type_name) for t in UserType.query.order_by("type_name")]
    if form.validate_on_submit():

        user = User(
            username=form.username.data, 
            email=form.email.data, 
            password=form.password.data, 
            enabled=form.enabled.data,
            user_type_id=form.user_type_id.data
        )

        db.session.add(user)
        db.session.commit()
        flash('Você foi registrado com sucesso! Agora você pode fazer login.')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title='Registro')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            if user.user_type.type_name == 'admin':
                return redirect(url_for('people.new_student'))
            else:
                return redirect(url_for('people.new_volunteer'))
        else:
            flash('Email ou senha inválidos.')

    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você fez logout com sucesso.')
    return redirect(url_for('auth.login'))