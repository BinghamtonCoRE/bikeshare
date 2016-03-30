"""Define the views for the app"""
from flask import render_template
from bikeshare_app import app
from bikeshare_app.models import ActiveShare

# Index page
# Lets just show what bikes are available and have a link to checkout a bike
@app.route("/")
def index():
    """Return the index page for the app"""
    return render_template('bikes.html', bikes=ActiveShare.objects(available=True))

# Admin page
# Display bike availabilities again. Ability to alter database info
@app.route("/admin")
def admin():
    """The admin page"""
    return "Admin page"

# Bike request endpoint
@app.route("/request_bike/<user_email>/<int:bike_id>")
def request_bike():
    """This endpoint is for requesting a bike"""
    return "Bike request"
