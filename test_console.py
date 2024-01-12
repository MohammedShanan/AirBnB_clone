#!/usr/bin/python3
"""
Unit Test for console
"""
import console
from contextlib import contextmanager
from datetime import datetime
import inspect
from io import StringIO
import models
import pep8
import sys
from os import environ, stat
import unittest

Place = models.place.Place
State = models.state.State
User = models.user.User
HBNBCommand = console.HBNBCommand
storage = console.storage
cls_init = models.cls_init


class TestHBNBcmdCreateUpdate(unittest.TestCase):
    """testing instantiation of CLI & create() function"""

    @classmethod
    def setUpClass(cls):
        """init: prints output to mark new tests"""
        storage.delete_all()
        print('...creating new Place object: ', end='')
        cls.cli = HBNBCommand()
        cls.cli.do_create('Place ')
        print('')
        cls.storage_objs = storage.all()
        for v in cls.storage_objs.values():
            cls.obj = v
        print(cls.obj)

    def setUp(self):
        """initializes new HBNBCommand instance for each test"""
        self.CLI = TestHBNBcmdCreateUpdate.cli
        self.obj = TestHBNBcmdCreateUpdate.obj

    def test_instantiation(self):
        """... checks if HBNBCommand CLI Object is properly instantiated"""
        self.assertIsInstance(self.CLI, HBNBCommand)

    def test_create(self):
        """... tests creation of class City with attributes"""
        self.assertIsInstance(self.obj, cls_init['Place'])

    def test_attr_user_id(self):
        """... checks if proper parameter for user_id was created"""
        self.CLI.do_update('Place {} user_id "o111"'.format(self.obj.id))
        actual = self.obj.user_id
        print(actual)
        expected = "o111"
        self.assertEqual(expected, actual)

    def test_attr_city_id(self):
        """... checks if proper parameter for city_id was created"""
        self.CLI.do_update('Place {} city_id "A1111"'.format(self.obj.id))
        actual = self.obj.city_id
        expected = "A1111"
        self.assertEqual(expected, actual)

    def test_attr_name(self):
        """... checks if proper parameter for name was created"""
        self.CLI.do_update('Place {} name "Ashina_castle"'.format(self.obj.id))
        actual = self.obj.name
        expected = 'Ashina_castle'
        self.assertEqual(expected, actual)

    def test_attr_num_rm(self):
        """... checks if proper parameter for number_rooms was created"""
        self.CLI.do_update('Place {} number_rooms 4'.format(self.obj.id))
        actual = self.obj.number_rooms
        expected = 4
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_num_btrm(self):
        """... checks if proper parameter for number_bathrooms was created"""
        self.CLI.do_update('Place {} number_bathrooms 2'.format(self.obj.id))
        actual = self.obj.number_bathrooms
        expected = 2
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_max_guest(self):
        """... checks if proper parameter for max_guest was created"""
        self.CLI.do_update('Place {} max_guest 10'.format(self.obj.id))
        actual = self.obj.max_guest
        expected = 10
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), int)

    def test_attr_price_bn(self):
        """... checks if proper parameter for price_by_night was created"""
        self.CLI.do_update('Place {} price_by_night 300'.format(self.obj.id))
        actual = self.obj.price_by_night
        expected = 300
        self.assertEqual(expected, actual)
        self.assertEqual(type(actual), int)

    def test_attr_lat(self):
        """... checks if proper parameter for latitude was created"""
        self.CLI.do_update('Place {} latitude 54.454'.format(self.obj.id))
        actual = self.obj.latitude
        expected = 54.454
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)

    def test_attr_long(self):
        """... checks if proper parameter for longitude was created"""
        self.CLI.do_update('Place {} longitude 14.4545'.format(self.obj.id))
        actual = self.obj.longitude
        expected = 14.4545
        self.assertEqual(expected, actual)
        self.assertIs(type(actual), float)


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
