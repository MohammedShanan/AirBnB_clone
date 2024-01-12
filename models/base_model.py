#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import models
from uuid import uuid4
from datetime import datetime
import json


class BaseModel():
    """
        attributes and functions for BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
            instantiation of new BaseModel Class
        """
        if kwargs:
            self.__set_attr(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def save(self):
        """
            private: converts attr_dict values to python class attributes
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def __is_serializable(self, obj_v):
        """
            private: checks if object is serializable
        """
        try:
            obj_to_str = json.dumps(obj_v)
            return obj_to_str is not None and isinstance(obj_to_str, str)
        except TypeError:
            return False

    def to_json_str(self):
        """
            returns json representation of self
        """
        obj_class = self.__class__.__name__
        bm_dict = {
            k: v if self.__is_serializable(v) else str(v)
            for k, v in self.__dict__.items()
        }
        bm_dict['__class__'] = obj_class
        return bm_dict

    def __str__(self):
        """
            returns string type representation of object instance
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def __repr__(self):
        """
            returns string type representation of object instance
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def __set_attr(self, attr_dict):
        """
            private: converts attr_dict values to python class attributes
        """
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid4)
        if 'created_at' not in attr_dict:
            attr_dict['created_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['created_at'], datetime):
            attr_dict['created_at'] = datetime.fromisoformat(
                attr_dict['created_at'])
        if 'updated_at' not in attr_dict:
            attr_dict['updated_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['updated_at'], datetime):
            attr_dict['updated_at'] = datetime.fromisoformat(
                attr_dict['updated_at'])
        if '__class__' in attr_dict.keys():
            attr_dict.pop('__class__')
        for attr, value in attr_dict.items():
            setattr(self, attr, value)

    def to_dict(self):
        """
            return a dictionary representation of the BaseModel
        """
        class_name = type(self).__name__
        dic = {"__class__": class_name}
        for key in self.__dict__:
            if key == 'updated_at' or key == 'created_at':
                dic[key] = datetime.isoformat(self.__dict__[key])
            else:
                dic[key] = self.__dict__[key]
        return dic

    def update_bm(self, attr_dict):
        """
            updates the BaseModel and sets the correct attributes
        """
        for attr, value in attr_dict.items():
            if attr not in ["id", "created_at", "updated_at"]:
                setattr(self, attr, value)
        self.save()
