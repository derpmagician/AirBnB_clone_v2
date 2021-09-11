#!/usr/bin/python3
""" flask """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """print"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cname(text):
    """print text"""
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run()
