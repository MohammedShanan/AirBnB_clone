#!/usr/bin/python3
from datetime import datetime
import json
import time
import unittest
import models
import pep8
from os import remove
Amenity = models.amenity.Amenity


class TestAmenityStyle(unittest.TestCase):
    def test_pep8(self):
        """amenity.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nAmenity Class from Models Module\n'
        actual = models.amenity.__doc__
        self.assertEqual(expected, actual)


class TestAmenity(unittest.TestCase):
    def tearDownClass():
        """tidies up the tests removing storage objects"""
        remove('file.json')

    def setUp(self):
        """initializes new Amenity instance for testing"""
        self.my_amenity = Amenity()

    def test_amenity_init(self):
        """checks if Amenity is properly instantiated"""
        self.assertNotEqual(self.my_amenity.id, None)
        self.assertNotEqual(self.my_amenity.created_at, None)
        self.assertNotEqual(self.my_amenity.updated_at, None)

    def test_named_attr(self):
        """add name attribute"""
        self.my_amenity.name = "Tekken 8!!!"
        self.assertEqual(self.my_amenity.name, "Tekken 8!!!")

    def test_save(self):
        """save function should add updated_at attribute"""
        prev_updated_at = self.my_amenity.updated_at
        time.sleep(0.1)
        self.my_amenity.save()
        curr_updated_at = self.my_amenity.updated_at
        self.assertNotEqual(curr_updated_at, prev_updated_at)

    def test_json_str(self):
        """to_json should include class key with value amenity"""
        my_amenity_json = self.my_amenity.to_json_str()
        actual = None
        if my_amenity_json['__class__']:
            actual = my_amenity_json['__class__']
        expected = 'Amenity'
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """to_dict should return a dictionary representation of class Amenity"""
        self.my_amenity.name = "Tekken 8!!!"
        amenity_dict = self.my_amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        keys = ['__class__', 'updated_at',
                'created_at', 'id', 'name']
        for i in keys:
            self.assertTrue(i in amenity_dict.keys())


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
