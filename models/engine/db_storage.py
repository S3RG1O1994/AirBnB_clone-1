#!/usr/bin/python3
'''File of method for use DB'''
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City


class DBStorage:
    """ DataBase engine for hbnb """
    __engine = None
    __session = None

    def __init__(self):
        """ engine constructor """
        MySQL_User = environ.get('HBNB_MYSQL_USER')
        MySQL_Pwd = environ.get('HBNB_MYSQL_PWD')
        MySQL_Host = environ.get('HBNB_MYSQL_HOST')
        MySQL_DB = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MySQL_User, MySQL_Pwd, MySQL_Host,
                                             MySQL_DB), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ display all objs of a class """
        coso = {}
        if cls is not None:
            for item in self.__session.query(cls).all():
                kay = "{}.{}".format(type(item).__name__, item.id)
                # coso.update({kay:item})
                coso[kay] = item
        else:
            clase = [City, State, User, Place, Review]  # Amenity
            for box in clase:
                for item in self.__session.query(box):
                    kay = "{}.{}".format(type(item).__name__, item.id)
                    # coso.update({kay:item})
                    coso[kay] = item
        return coso

    def new(self, obj):
        """ add a new instance in DB """
        self.__session.add(obj)

    def save(self):
        """ commit in session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete instance """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ re-load DB """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''Method class for use remove session'''
        self.__session.remove()
