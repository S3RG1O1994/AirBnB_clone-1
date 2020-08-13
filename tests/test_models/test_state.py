#!/usr/bin/python3
''' User unittesting '''

import unittest
import pep8
import json
import os
from datetime import datetime
from models import state
from models.base_model import BaseModel


class TestUserDocu(unittest.TestCase):
    ''' test Base Documentation '''

    def test_pep8(self):
        """ Test that models/base_model.py conforms to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix Your PEP8 Style")

    def test_pep8_base(self):
        """ Test the test file xD """
        pep8style = pep8.StyleGuide(quiet=True)
        r = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(r.total_errors, 0, "Fix Your PEP8 Style")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(state.State.__doc__)

    def test_docmodule(self):
        """ Tests module """
        self.assertTrue(len(state.__doc__) >= 1)


class TestUser(unittest.TestCase):
    ''' Test base class '''

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
        obj = state.State()
        self.assertTrue(issubclass(type(obj), BaseModel))

    def test_typos(self):
        ''' check for attributes '''
        obj = state.State()
        self.assertEqual(type(obj.name), str)
        self.assertEqual(type(obj.id), str)
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)
        self.assertEqual(obj.__class__.__name__, 'State')

    def test_verify_attr(self):
        ''' check for attributes '''
        obj = state.State()
        self.assertTrue(hasattr(obj, 'name'))
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertEqual(obj.__class__.__name__, 'State')

    def test_kwargs(self):
        """Test the class - BaseModel passing kwargs """
        dictionary = {'id': '662a23b3-abc7-4f43-81dc-64c000000c00'}
        user1 = state.State(**dictionary)
        self.assertTrue(issubclass(user1.__class__, BaseModel))
