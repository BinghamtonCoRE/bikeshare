from bikeshare_app import app
# Dont call app.run(). Uwsgi will do this for us

if __name__ == "__main__":
    app.run()
