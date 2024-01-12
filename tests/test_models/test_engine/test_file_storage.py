#!/usr/bin/python3
"""
Unit Test for File storage Class
"""
import unittest
import json
import models
from models import engine
from models.engine.file_storage import FileStorage
import pep8
from os import remove, path

BaseModel = models.base_model.BaseModel
State = models.state.State
storage = models.storage
file_name = './file.json'


class TestFileStorageStyle(unittest.TestCase):

    def test_file_storage_pep8(self):
        """file_storage.py conforms to PEP8 Style"""
        pep8style = pep8.StyleGuide(quit=True)
        errors = pep8style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_doc_file(self):
        """documentation for the file"""
        expected = ("\nHandles I/O, writing and reading, of JSON for storage "
                    "of all class instances\n")
        actual = models.file_storage.__doc__
        self.assertEqual(expected, actual)


class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        storage.delete_all()
        if path.isfile(file_name):
            remove(file_name)
        cls.bm_obj = BaseModel()
        cls.state_obj = State()
        cls.state_obj.name = "Tennessee"
        cls.bm_obj.save()
        cls.state_obj.save()

    def tearDownClass():
        """tidies up the tests removing storage objects"""
        storage.delete_all()
        remove(file_name)

    def setUp(self):
        """initializes new storage object for testing"""
        self.bm_obj = TestFileStorage.bm_obj
        self.state_obj = TestFileStorage.state_obj
        self.bm_obj.save()
        self.state_obj.save()

    def tearDown(self):
        """tidies up the tests removing storage objects"""
        remove(file_name)

    def test_storage_file_exists(self):
        """checks proper FileStorage instantiation"""
        self.assertTrue(path.isfile(file_name))

    def test_all(self):
        """checks if all() function returns newly created instances"""
        obj_id_list = [self.state_obj.id, self.bm_obj.id]
        obj_dict = storage.all()
        for obj in obj_dict.values():
            self.assertTrue(obj.id in obj_id_list)

    def test_obj_saved_to_file(self):
        """checks proper FileStorage instantiation"""
        new_obj = BaseModel()
        new_obj.save()
        cls_name = new_obj.__class__.__name__
        with open(file_name, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        actual = False
        for v in storage_dict.values():
            if v['__class__'] == cls_name and v['id'] == new_obj.id:
                actual = True
        self.assertTrue(actual)

    def test_new(self):
        """checks if new function add new obj to the __objects variable"""
        new_obj = BaseModel()
        storage.new(new_obj)
        storage_dict = storage.all()
        self.assertTrue(new_obj in storage_dict.values())

    def test_delete(self):
        """checks if delete function removes obj from the __objects variable"""
        new_obj = BaseModel()
        storage.new(new_obj)
        storage_dict = storage.all()
        actual = new_obj in storage_dict.values()
        storage.delete(new_obj)
        actual = new_obj in storage_dict.values()
        self.assertFalse(actual)

    def test_reload(self):
        """checks proper usage of reload function"""
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        id = self.bm_obj.id
        actual = False
        for v in all_obj.values():
            if v.id == id:
                actual = True
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
