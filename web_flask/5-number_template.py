#!/usr/bin/python3
"""first flask hello world"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """basic index page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """extra page /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """create page /c/text """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={"text": "is cool"},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """create page /python/text """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """create page /number """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ create page /number_template"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
