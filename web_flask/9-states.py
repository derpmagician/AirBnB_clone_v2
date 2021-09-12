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


@app.route('/states/')
@app.route('/states/<st_id>', strict_slashes=False)
def states_id(state_id=None):
    """Lists states by cities"""
    states = storage.all(State)
    if st_id != None:
        st_id = 'State.' + st_id
    return render_template('9-states.html', states=states, st_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
