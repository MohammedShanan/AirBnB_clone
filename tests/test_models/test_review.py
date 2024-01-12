#!/usr/bin/python3
from datetime import datetime
import json
import time
import unittest
import models
import pep8
from os import remove
Review = models.review.Review


class TestReviewStyle(unittest.TestCase):
    def test_pep8(self):
        """review.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/review.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nReview Class from Models Module\n'
        actual = models.review.__doc__
        self.assertEqual(expected, actual)


class TestReview(unittest.TestCase):
    def tearDownClass():
        """tidies up the tests removing storage objects"""
        remove('file.json')
    def setUp(self):
        """initializes new Review instance for testing"""
        self.my_review = Review()

    def test_review_init(self):
        """checks if Review is properly instantiated"""
        self.assertNotEqual(self.my_review.id, None)
        self.assertNotEqual(self.my_review.created_at, None)
        self.assertNotEqual(self.my_review.updated_at, None)

    def test_named_attr(self):
        """add name attribute"""
        self.my_review.user_id = "007"
        self.my_review.place_id = "OO7"
        self.my_review.text = "This is a great place to be a spy!!!"
        self.assertEqual(self.my_review.user_id, "007")
        self.assertEqual(self.my_review.place_id, "OO7")
        self.assertEqual(self.my_review.text,
                         "This is a great place to be a spy!!!")

    def test_save(self):
        """save function should add updated_at attribute"""
        prev_updated_at = self.my_review.updated_at
        time.sleep(0.1)
        self.my_review.save()
        curr_updated_at = self.my_review.updated_at
        self.assertNotEqual(curr_updated_at, prev_updated_at)

    def test_json_str(self):
        """to_json should include class key with value review"""
        my_review_json = self.my_review.to_json_str()
        actual = None
        if my_review_json['__class__']:
            actual = my_review_json['__class__']
        expected = 'Review'
        self.assertEqual(expected, actual)

    def test_to_dict(self):
        """to_dict should return a dictionary representation of class Review"""
        self.my_review.user_id = "007"
        self.my_review.place_id = "OO7"
        self.my_review.text = "This is a great place to be a spy!!!"
        review_dict = self.my_review.to_dict()
        self.assertIsInstance(review_dict, dict)
        keys = ['__class__', 'updated_at',
                'created_at', 'id', 'user_id', 'place_id', 'text']
        for i in keys:
            self.assertTrue(i in review_dict.keys())


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main()
