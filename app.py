"""Helper to run the app"""
from os import getenv
from bikeshare_app import app

if __name__ == "__main__":
    port = getenv("PORT", 8000)
    app.run(host="0.0.0.0", port=port)
