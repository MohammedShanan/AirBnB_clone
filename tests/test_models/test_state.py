#!/usr/bin/python3
from datetime import datetime
import json
import time
import unittest
import models
import pep8
from os import remove
State = models.state.State


class TestStateStyle(unittest.TestCase):
    def test_pep8(self):
        """state.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/state.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nState Class from Models Module\n'
        actual = models.state.__doc__
        self.assertEqual(expected, actual)


class TestState(unittest.TestCase):
    def tearDownClass():
        """tidies up the tests removing storage objects"""
        remove('file.json')
    def setUp(self):
        """initializes new State instance for testing"""
        self.my_state = State()

    def test_state_init(self):
        """checks if State is properly instantiated"""
        self.assertNotEqual(self.my_state.id, None)
        self.assertNotEqual(self.my_state.created_at, None)
        self.assertNotEqual(self.my_state.updated_at, None)

    def test_named_attr(self):
        """add name attribute"""
        self.my_state.name = "Tennessee"
        self.assertEqual(self.my_state.name, "Tennessee")

    def test_save(self):
        """save function should add updated_at attribute"""
        prev_updated_at = self.my_state.updated_at
        time.sleep(0.1)
        self.my_state.save()
        curr_updated_at = self.my_state.updated_at
        self.assertNotEqual(curr_updated_at, prev_updated_at)

    def test_json_str(self):
        """to_json should include class key with value state"""
        my_state_json = self.my_state.to_json_str()
        actual = None
        if my_state_json['__class__']:
            actual = my_state_json['__class__']
        expected = 'State'
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """to_dict should return a dictionary representation of class State"""
        self.my_state.name = "Tennessee"
        state_dict = self.my_state.to_dict()
        self.assertIsInstance(state_dict, dict)
        keys = ['__class__', 'updated_at',
                'created_at', 'id', 'name']
        for i in keys:
            self.assertTrue(i in state_dict.keys())


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
