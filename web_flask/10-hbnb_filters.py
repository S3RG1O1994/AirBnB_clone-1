#!/usr/bin/python3
'''This function is for edit html'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters/', strict_slashes=False)
def filters():
    '''Render page'''
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                        s_list=states.values(),
                        a_list=amenities.values()
                        )

@app.teardown_appcontext
def close(exception):
    '''Close session in SQLAlchemy'''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
