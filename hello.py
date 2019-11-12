"""Minmal flask app"""

from flask import Flask, render_template

# Make App
app = Flask(__name__)

# Make default route
@app.route("/")

# Making the first function
def hello():
    return render_template('home.html')

# Creating another route
@app.route("/about")

def info():
    return render_template('about.html')