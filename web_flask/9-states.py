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
def states_id(id):
    """Lists states by cities"""
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            return render_template('9-states.html',
                                   state=state, state_cities=state.cities)

    return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
