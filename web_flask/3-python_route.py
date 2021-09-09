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

@app.route('/c/<name>', strict_slashes=False)
def cname(name):
    """print name"""
    return 'C {}'.format(name.replace('_', ' '))

if __name__ == '__main__':
    app.run()
