#!/usr/bin/python3

"""
flask
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """print"""
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """no hellow"""
    return ("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
