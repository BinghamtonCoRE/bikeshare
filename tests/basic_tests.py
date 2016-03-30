import flask
from bikeshare_app import app


def test_home():
    """Stupid simple test for the home page."""
    with app.test_request_context("/"):
        assert flask.request.path == "/"

def test_admin():
    """Stupid simple test for the admin page."""
    with app.test_request_context("/admin"):
        assert flask.request.path == "/admin"
