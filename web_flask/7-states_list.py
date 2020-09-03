#!/usr/bin/python3
'''This function is for edit html'''
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def index():
    '''This return string in the page'''
    states = storage.all()
    states = states.values()
    return render_template(
        '7-states_list.html',
        s_list=states
    )

@app.teardown_appcontext
def close():
    '''Close session in SQLAlchemy'''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
