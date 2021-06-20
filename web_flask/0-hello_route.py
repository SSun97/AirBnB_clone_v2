#!/usr/bin/python3
"""the first flask page"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """most basic index page """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
