#!/usr/bin/python3
"""first flask hello world"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """basic index page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """extra page /hbnb"""
    return "HBNB"

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
