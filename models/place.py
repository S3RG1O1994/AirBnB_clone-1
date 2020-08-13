#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table(
    'place_amenity', 
    Base.metadata, 
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True), 
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade="all, delete, delete-orphan", backref='place')
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
    else:
        @property
        def reviews(self):
            ret_list = []
            review_dir = models.storage.all(Review)
            for sub_dir in review_dir.values():
                if sub_dir.place_id is self.id:
                    ret_list.append(sub_dir)
            return ret_list
        
        @property
        def amenities(self):
            ret_list = []
            amenitie_dir = models.storage.all(Amenity)
            for sub_dir in amenitie_dir.values():
                if sub_dir.place_id is self.id:
                    ret_list.append(sub_dir)
            return ret_list

        @amenities.setter
        def amenities(self, Amenity_obj=None):
            if isinstance(Amenity_obj, models.Amenity):
                self.amenity_ids.append(Amenity_obj.id)