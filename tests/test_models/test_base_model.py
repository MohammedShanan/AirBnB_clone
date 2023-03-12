#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
from datetime import datetime
import json
import time
import unittest
import models
import pep8
from os import remove
BaseModel = models.base_model.BaseModel


class TestBaseModelStyle(unittest.TestCase):
    def test_pep8(self):
        """base_model.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nBaseModel Class of Models Module\n'
        actual = models.base_model.__doc__
        self.assertEqual(expected, actual)


class TestBaseModel(unittest.TestCase):
    def tearDownClass():
        """tidies up the tests removing storage objects"""
        remove('file.json')

    def setUp(self):
        """initializes new BaseModel instance for testing"""
        self.my_model = BaseModel()

    def test_base_model_init(self):
        """checks if BaseModel is properly instantiated"""
        self.assertNotEqual(self.my_model.id, None)
        self.assertNotEqual(self.my_model.created_at, None)
        self.assertNotEqual(self.my_model.updated_at, None)

    def test_named_attr(self):
        """add name attribute"""
        self.my_model = BaseModel()
        self.my_model.name = "mohammed"
        self.assertEqual(self.my_model.name, "mohammed")

    def test_number_attr(self):
        """add number attribute"""
        self.my_model.number = 3
        self.assertEqual(self.my_model.number, 3)

    def test_save(self):
        """save function should add updated_at attribute"""
        prev_updated_at = self.my_model.updated_at
        time.sleep(0.1)
        self.my_model.save()
        curr_updated_at = self.my_model.updated_at
        self.assertNotEqual(curr_updated_at, prev_updated_at)

    def test_json_str(self):
        """... to_json should include class key with value BaseModel"""
        my_model_json = self.my_model.to_json_str()
        actual = None
        if my_model_json['__class__']:
            actual = my_model_json['__class__']
        expected = 'BaseModel'
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """to_dict should return a dictionary representation of class BaseModel"""
        model_dict = self.my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        keys = ['__class__', 'updated_at', 'created_at', 'id']
        for i in keys:
            self.assertTrue(i in model_dict.keys())


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
