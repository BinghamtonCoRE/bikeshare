"""Define the views for the app"""
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import flask.ext.login as flask_login
from . import app
from . import login_manager
from .models import ActiveShare
from os import getenv


class User(flask_login.UserMixin):
    """User model for login."""
    pass


@login_manager.user_loader
def user_loader(email):
    """Load a user from a session."""
    # TODO: Hookup email verification to DB, verify they exist
    user = User()
    user.id = email
    return user


# Lets just show what bikes are available and have a link to checkout a bike
@app.route('/')
def index():
    """Return the index page for the app"""
    return render_template('bikes.html',
                           bikes=ActiveShare.objects(available=True))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Allow user through if check passed, else log attempt and return home
        return render_template('login.html')
    email = request.form['email']
    if request.form['pass'] == getenv('BIKESHARE_ADMIN_PASSWORD'):
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('admin'))
    return redirect(url_for('index'))


@app.route('/logout')
@flask_login.login_required
def logout():
    """Logout route."""
    flask_login.logout_user()
    return redirect(url_for('index'))


# Admin page
# Display bike availabilities again. Ability to alter database info
@app.route('/admin')
@flask_login.login_required
def admin():
    """The admin page"""
    return render_template('admin.html')


@app.route('/request_bike/<user_email>/<int:bike_id>')
def request_bike():
    """This endpoint is for requesting a bike"""
    return 'Bike request'
