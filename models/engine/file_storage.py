#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
import os
from models import base_model, user, state, city, place, amenity, review


class FileStorage():
    """
        handles long term storage of all class instances
    """
    cls_init = {
        'BaseModel': base_model.BaseModel,
        'User': user.User,
        'City': city.City,
        'State': state.State,
        'Place': place.Place,
        'Amenity': amenity.Amenity,
        'Review': review.Review
    }
    """cls_init - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """
    __file_path = './file.json'
    __objects = {}

    def all(self):
        """
            returns private attribute: __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets / updates in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        fname = FileStorage.__file_path
        storage_dict = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            storage_dict[bm_id] = bm_obj.to_json_str()
        with open(fname, mode='w', encoding="utf-8") as f:
            json.dump(storage_dict, f)

    def reload(self):
        """
            if file exists, deserializes JSON file to __objects, else nothing
        """
        fname = FileStorage.__file_path
        try:
            with open(fname, mode="r", encoding='utf-8') as f:
                new_objs = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return
        for obj_id, obj_dict in new_objs.items():
            cls_name = obj_dict['__class__']
            obj_dict = FileStorage.cls_init[cls_name](**obj_dict)
            FileStorage.__objects[obj_id] = obj_dict

    def delete(self, obj):
        """
            deletes obj from __objects if it's inside
        """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        del FileStorage.__objects[obj_key]
        self.save()

    def delete_all(self):
        """
            deletes all stored objects, for testing purposes
        """
        del FileStorage.__objects
        FileStorage.__objects = {}
        self.save()
