from flask import Flask
from .models import DB

# now I made a app factory

def create_app():
    app = Flask(__name__)

    # Add config
    app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///df.sqlite3"

    # Have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff'
    return app