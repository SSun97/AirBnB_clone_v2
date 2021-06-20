#!/usr/bin/python3
"""project about flask"""

from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def closedb(func):
    """Closes session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """page for /states_list"""
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
