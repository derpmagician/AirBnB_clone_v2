#!/usr/bin/python3
""" flask """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list_all():
    """ List States """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run()
