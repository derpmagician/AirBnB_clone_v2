#!/usr/bin/python3
""" flask """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
def states_id(state_id=None):
    """Lists states by cities"""
    states = storage.all(State).values()
    if state_id != None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    app.run()
