#!/usr/bin/python3
'''This function is for edit html'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def index_states():
    '''List of cities for group by states'''
    states = storage.all(State)
    return render_template(
        '8-cities_by_states.html',
        states=states
    )


@app.teardown_appcontext
def close():
    '''Close session in SQLAlchemy'''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
