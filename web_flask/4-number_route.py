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
def ctext(text):
    """print text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    """print text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def nnumber(n):
    """"Print number"""
    if isinstance(n, int):
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run()
