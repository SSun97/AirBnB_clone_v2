#!/usr/bin/python3
"""Project about using flask"""

from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def closedb(foo):
    """Closes session"""
    storage.close()


@app.route('/states', strict_slashes=False, defaults={'id': None})
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """create page /states"""
    state = states = None
    if id:
        states = storage.all(State)
        key = "State." + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    else:
        states = list(storage.all(State).values())
    return render_template('9-states.html', **locals())


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
