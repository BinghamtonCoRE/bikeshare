from bikeshare_app import app
from bikeshare_app.models import ActiveShare
from flask import render_template

# Index page
# Lets just show what bikes are available and have a link to checkout a bike
@app.route("/")
def index():
    return render_template('bikes.html', bikes=ActiveShare.objects(available=True))

# Admin page
# Display bike availabilities again. Ability to alter database info
@app.route("/admin")
def admin():
    #TODO Check user credentials for admin role
    # Allow user through if check passed, else log attempt and return home
    return render_template('admin.html')

# Bike request endpoint
@app.route("/request_bike/<user_email>/<int:bike_id>")
def request_bike():
    # TODO Handle logic for requesting a bike
    # Return result object that the future template will use
    return render_template('request_bike.html', bike_id=bike_id)
