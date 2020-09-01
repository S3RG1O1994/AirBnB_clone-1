#!/usr/bin/python3
from flask import Flask
'''This function is for edit html'''

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''This return string in the page'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index_hbtn():
    '''This return string in the page'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
