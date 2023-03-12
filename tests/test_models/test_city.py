#!/usr/bin/python3
from datetime import datetime
import json
import time
import unittest
import models
import pep8
from os import remove

City = models.city.City


class TestCityStyle(unittest.TestCase):
    def test_pep8(self):
        """city.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/city.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nCity Class from Models Module\n'
        actual = models.city.__doc__
        self.assertEqual(expected, actual)


class TestCity(unittest.TestCase):
    def tearDownClass():
        """tidies up the tests removing storage objects"""
        remove('file.json')

    def setUp(self):
        """initializes new City instance for testing"""
        self.my_city = City()

    def test_city_init(self):
        """checks if City is properly instantiated"""
        self.assertNotEqual(self.my_city.id, None)
        self.assertNotEqual(self.my_city.created_at, None)
        self.assertNotEqual(self.my_city.updated_at, None)

    def test_named_attr(self):
        """add name attribute"""
        self.my_city.name = "New York"
        self.my_city.state_id = "00ABC"
        self.assertEqual(self.my_city.name, "New York")
        self.assertEqual(self.my_city.state_id, "00ABC")

    def test_save(self):
        """save function should add updated_at attribute"""
        prev_updated_at = self.my_city.updated_at
        time.sleep(0.1)
        self.my_city.save()
        curr_updated_at = self.my_city.updated_at
        self.assertNotEqual(curr_updated_at, prev_updated_at)

    def test_json_str(self):
        """to_json should include class key with value City"""
        my_city_json = self.my_city.to_json_str()
        actual = None
        if my_city_json['__class__']:
            actual = my_city_json['__class__']
        expected = 'City'
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """to_dict should return a dictionary representation of class City"""
        self.my_city.name = "New York"
        self.my_city.state_id = "00ABC"
        city_dict = self.my_city.to_dict()
        self.assertIsInstance(city_dict, dict)
        keys = ['__class__', 'updated_at',
                'created_at', 'id', 'state_id', 'name']
        for i in keys:
            self.assertTrue(i in city_dict.keys())


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
