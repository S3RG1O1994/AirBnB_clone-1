#!/usr/bin/python3
''' User unittesting '''

import unittest
import pep8
import json
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
import os


class TestCitydocu(unittest.TestCase):
    ''' test Base Documentation '''

    def test_pep8(self):
        """ Test that models/base_model.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix Your PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(r.total_errors, 0, "Fix Your PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(City.__doc__) >= 1)


class TestCity(unittest.TestCase):
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
        obj = City()
        self.assertTrue(issubclass(type(obj), BaseModel))

    def test_typos(self):
        ''' check for attributes '''
        obj = City()
        self.assertEqual(type(obj.state_id), str)
        self.assertEqual(type(obj.id), str)
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)
        self.assertEqual(obj.__class__.__name__, 'City')

    def test_verify_attr(self):
        ''' check for attributes '''
        obj = City()
        self.assertTrue(hasattr(obj, 'state_id'))
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictonary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        user1 = City(**dictonary)
        self.assertTrue(issubclass(user1.__class__, BaseModel))
