"""Define the views for the app"""
from os import getenv
from flask import render_template, request, redirect, url_for, flash
import flask.ext.login as flask_login
from . import app
from . import login_manager
from .models import ActiveShare


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
    app.logger.debug('Rendering index page')
    return render_template('bikes.html',
                           bikes=ActiveShare.objects(available=True))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Page to both login and process logins"""
    if request.method == 'GET':
        # Allow user through if check passed, else log attempt and return home
        return render_template('login.html')
    email = request.form['email']
    if request.form['passwd'] == getenv('BIKESHARE_ADMIN_PASSWORD'):
        user = User()
        user.id = email
        flask_login.login_user(user)
        flash('Admin login successful')
        return redirect(url_for('admin'))
    flash('Invalid password')
    return redirect(url_for('index'))


@app.route('/logout')
@flask_login.login_required
def logout():
    """Logout route."""
    flask_login.logout_user()
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/admin')
@flask_login.login_required
def admin():
    """The admin page.

    Display the bike availabilities again. Also add ability to alter
    the DB's
    """
    app.logger.debug('Rendering admin page')
    # TODO Check user credentials for admin role
    # Allow user through if check passed, else log attempt and return home
    return render_template('admin.html')

@app.route("/request_bike/<user_email>/<int:bike_id>")
def request_bike(user_email, bike_id):
    """This endpoint is for requesting a bike"""
    app.logger.debug('User {} requesting bike {}'.format(user_email, bike_id))
    return render_template('admin.html')
