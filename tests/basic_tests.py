import flask
from bikeshare_app import app


def test_home():
    """Stupid simple test."""
    with app.test_request_context("/"):
        assert flask.request.path == "/"
