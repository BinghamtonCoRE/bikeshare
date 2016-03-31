from bikeshare_app import create_app
# Dont call app.run(). Uwsgi will do this for us

if __name__ == "__main__":
    app = create_app()
    app.run()
