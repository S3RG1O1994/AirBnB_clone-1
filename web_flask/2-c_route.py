#!/usr/bin/python3
'''This function is for edit html'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''This return string in the page'''
    return 'HBNB'


@app.route('/hbnb', strict_slashes=False)
def index_hbnb():
    '''This return string in the page'''
    return 'Hello HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def index_c(text):
    '''This is return string pass in text'''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
