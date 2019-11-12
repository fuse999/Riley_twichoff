"""Minmal flask app"""

from flask import Flask

# Make App
app = Flask(__name__)

# Make default route
@app.route("/")

# Making the first function
def hello():
    return "Hello World"