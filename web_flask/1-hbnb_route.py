#!/usr/bin/python3
'''This function is for edit html'''
from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def index_hbtn():
    '''This return string in the page'''
    return 'HBNB'


@app.route('/', strict_slashes=False)
def index():
    '''This return string in the page'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
