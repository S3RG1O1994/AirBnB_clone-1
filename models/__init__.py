#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.db_storage import  DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ

Data_type = environ.get('HBNB_TYPE_STORAGE')
if Data_type is not None and Data_type in 'db':
    # print("aqui entro ;) {} ".format(db))
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
