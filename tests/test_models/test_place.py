#!/usr/bin/python3
from datetime import datetime
import json
import time
import unittest
import models
import pep8
from os import remove
Place = models.place.Place


class TestPlaceStyle(unittest.TestCase):
    def test_pep8(self):
        """place.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/place.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nPlace Class from Models Module\n'
        actual = models.place.__doc__
        self.assertEqual(expected, actual)


class TestPlace(unittest.TestCase):
    def tearDownClass():
        """tidies up the tests removing storage objects"""
        remove('file.json')
    def setUp(self):
        """initializes new Place instance for testing"""
        self.my_place = Place()

    def test_place_init(self):
        """checks if Place is properly instantiated"""
        self.assertNotEqual(self.my_place.id, None)
        self.assertNotEqual(self.my_place.created_at, None)
        self.assertNotEqual(self.my_place.updated_at, None)

    def test_named_attr(self):
        """add name attribute"""
        self.my_place.name = "Mishima dojo"
        self.my_place.user_id = "007"
        self.my_place.number_rooms = 8
        self.my_place.number_bathrooms = 4
        self.assertEqual(self.my_place.name, "Mishima dojo")
        self.assertEqual(self.my_place.user_id, "007")
        self.assertEqual(self.my_place.number_rooms, 8)
        self.assertEqual(self.my_place.number_bathrooms, 4)

    def test_save(self):
        """save function should add updated_at attribute"""
        prev_updated_at = self.my_place.updated_at
        time.sleep(0.1)
        self.my_place.save()
        curr_updated_at = self.my_place.updated_at
        self.assertNotEqual(curr_updated_at, prev_updated_at)

    def test_json_str(self):
        """to_json should include class key with value place"""
        my_place_json = self.my_place.to_json_str()
        actual = None
        if my_place_json['__class__']:
            actual = my_place_json['__class__']
        expected = 'Place'
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """to_dict should return a dictionary representation of class Place"""
        self.my_place.name = "Mishima dojo"
        self.my_place.user_id = "007"
        self.my_place.number_rooms = 8
        self.my_place.number_bathrooms = 4
        place_dict = self.my_place.to_dict()
        self.assertIsInstance(place_dict, dict)
        keys = ['__class__', 'updated_at',
                'created_at', 'id', 'name', 'user_id',
                'number_rooms', 'number_bathrooms']
        for i in keys:
            self.assertTrue(i in place_dict.keys())


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
