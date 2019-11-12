from flask import Flask

# now I made a app factory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff'
    return app