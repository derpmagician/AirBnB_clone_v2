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


@app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        """List States by City"""
        states = storage.all(State).values()
        cities = list()

        for state in states:
            for city in state.cities:
                cities.append(city)

        return render_template('8-cities_by_states.html',
                               states=states, state_cities=cities)


if __name__ == '__main__':
    app.run()
