#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    #if environ.get('HBNB_TYPE_STORAGE') == 'db':
    cities = relationship('City', cascade="all, delete, delete-orphan", backref='state')
    #else:
    @property
    def cities(self):
        ret_list = []
        city_dir = models.storage.all(City)
        for sub_dir in city_dir.values():
            if sub_dir.state_id is self.id:
                ret_list.append(sub_dir)
        return ret_list
