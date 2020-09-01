#!/usr/bin/python3
from flask import Flask
'''This function is for edit html'''

app = Flask(__name__)


@app.route('/hbnb')
def index():
    '''This return string in the page'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
