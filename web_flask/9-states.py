#!/usr/bin/python3
'''This function is for edit html'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/state/', strict_slashes=False)
@app.route('/state/<id>', strict_slashes=False)
def index_states():
    '''List of states'''
    states = storage.all(State)
    
    if not id:
        states = states.values()
        return render_template(
            '7-states_list.html',
            s_list=states
        )
    state = 'State.{}'.format(id)
    if state in states:
        return render_template('9-state.html', title='State: {}'.format(
            states[state].name, s_list=states[state]
        ))
    return render_template('9-state.html', s_list=None)


@app.teardown_appcontext
def close():
    '''Close session in SQLAlchemy'''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
