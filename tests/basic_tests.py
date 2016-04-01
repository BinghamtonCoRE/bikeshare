import flask
from bikeshare_app import app
from os import getenv


def test_home():
    """Stupid simple test for the home page."""
    with app.test_request_context("/"):
        assert flask.request.path == "/"


class TestAdmin():
    @classmethod
    def setup_class(cls):
        print(__name__, 'TestAdmin.setup_class() ------')

    @classmethod
    def teardown_class(cls):
        print(__name__, 'TestAdmin.teardown_class() ------')

    def setup(self):
        """Get test client for HTTP methods"""
        self.app = app.test_client()

    def login(self, email, password):
        """Simulate a POST to /login with credentials"""
        return self.app.post('/login', data=dict(email=email, passwd=password),
                             follow_redirects=True)

    def logout(self):
        """Simulate a logout"""
        return self.app.get('/logout', follow_redirects=True)

    def admin(self):
        """Try to access the admin page"""
        return self.app.get('/admin', follow_redirects=True)

    def test_admin_log_in(self):
        """Test the login endpoint to access admin"""
        rv = self.login('admin', 'MIDNA')
        assert b'Available Bikes' in rv.data
        rv = self.admin()
        # Make sure you're not authorized
        assert rv.status_code == 401
        rv = self.logout()
        # Can't logout if you're not logged in
        assert rv.status_code == 401
        rv = self.login('admin', getenv('BIKESHARE_ADMIN_PASSWORD'))
        assert b'Welcome to the admin panel!' in rv.data
        rv = self.admin()
        assert b'Welcome to the admin panel!' in rv.data
        rv = self.logout()
        assert b'Available Bikes' in rv.data
        rv = self.admin()
        # Make sure you're not authorized anymore
        assert rv.status_code == 401
