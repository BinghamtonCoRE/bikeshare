"""Define the views for the app"""
from flask import render_template
from bikeshare_app import app
from bikeshare_app.models import ActiveShare

# Index page
# Lets just show what bikes are available and have a link to checkout a bike
@app.route("/")
def index():
    """Return the index page for the app"""
    app.logger.debug('Rendering index page')
    return render_template('bikes.html', bikes=ActiveShare.objects(available=True))

# Admin page
# Display bike availabilities again. Ability to alter database info
@app.route("/admin")
def admin():
    """The admin page"""
    app.logger.debug('Rendering admin page')
    #TODO Check user credentials for admin role
    # Allow user through if check passed, else log attempt and return home
    return render_template('admin.html')

# Bike request endpoint
@app.route("/request_bike/<user_email>/<int:bike_id>")
def request_bike(user_email, bike_id):
    """This endpoint is for requesting a bike"""
    app.logger.debug('User %s requesting bike %d' % user_email, bike_id)
    return "Bike request"
