#!/usr/bin/python3
''' User unittesting '''

import unittest
import pep8
import json
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenitydocu(unittest.TestCase):
    ''' test Base Documentation '''

    def test_pep8(self):
        """ Test that models/base_model.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix Your PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(r.total_errors, 0, "Fix Your PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(Amenity.__doc__) >= 1)


class TestUser(unittest.TestCase):
    """ Test base class """

    @classmethod
    def setUpClass(cls):
        '''
        is called with the class as the only argument
        and must be decorated as a classmethod():
        '''
        pass

    @classmethod
    def tearDown(cls):
        ''' After tests, remove json file '''
        try:
            remove("file.json")
        except Exception:
            pass

    def test_subClass(self):
        '''Check if object have inheritance of the superclass'''
        obj = Amenity()
        self.assertTrue(issubclass(type(obj), BaseModel))

    def test_typos(self):
        ''' check for attributes '''
        obj = Amenity()
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.id), str)
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)
        self.assertEqual(obj.__class__.__name__, 'Amenity')

    def test_verify_attr(self):
        ''' check for attributes '''
        obj = Amenity()
        self.assertTrue(hasattr(obj, 'name'))
        self.assertEqual(type(obj.id), str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        user1 = Amenity(**dictonary)
        self.assertTrue(issubclass(user1.__class__, BaseModel))
