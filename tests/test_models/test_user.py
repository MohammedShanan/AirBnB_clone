#!/usr/bin/python3
from datetime import datetime
import json
import time
import unittest
import models
import pep8
from os import remove
User = models.user.User


class TestUserStyle(unittest.TestCase):
    def test_pep8(self):
        """user.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/user.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nUser Class from Models Module\n'
        actual = models.user.__doc__
        self.assertEqual(expected, actual)


class TestUser(unittest.TestCase):
    def tearDownClass():
        """tidies up the tests removing storage objects"""
        remove('file.json')
    def setUp(self):
        """initializes new User instance for testing"""
        self.my_user = User()

    def test_user_init(self):
        """checks if User is properly instantiated"""
        self.assertNotEqual(self.my_user.id, None)
        self.assertNotEqual(self.my_user.created_at, None)
        self.assertNotEqual(self.my_user.updated_at, None)

    def test_named_attr(self):
        """add name attribute"""
        self.my_user.first_name = "kazuya"
        self.my_user.last_name = "Mishima"
        self.my_user.email = "kazuyaMishima@tekken.com"
        self.my_user.password = "dorya"
        self.assertEqual(self.my_user.first_name, "kazuya")
        self.assertEqual(self.my_user.last_name, "Mishima")
        self.assertEqual(self.my_user.password, "dorya")
        self.assertEqual(self.my_user.email, "kazuyaMishima@tekken.com")

    def test_save(self):
        """save function should add updated_at attribute"""
        prev_updated_at = self.my_user.updated_at
        time.sleep(0.1)
        self.my_user.save()
        curr_updated_at = self.my_user.updated_at
        self.assertNotEqual(curr_updated_at, prev_updated_at)

    def test_json_str(self):
        """to_json should include class key with value user"""
        my_user_json = self.my_user.to_json_str()
        actual = None
        if my_user_json['__class__']:
            actual = my_user_json['__class__']
        expected = 'User'
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """to_dict should return a dictionary representation of class User"""
        self.my_user.first_name = "kazuya"
        self.my_user.last_name = "Mishima"
        self.my_user.email = "kazuyaMishima@tekken.com"
        self.my_user.password = "dorya"
        user_dict = self.my_user.to_dict()
        self.assertIsInstance(user_dict, dict)
        keys = ['__class__', 'updated_at',
                'created_at', 'id', 'first_name', 'last_name', 'password', 'email']
        for i in keys:
            self.assertTrue(i in user_dict.keys())


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
