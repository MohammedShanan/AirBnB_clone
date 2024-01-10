#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""
import models
import json
import uuid
from datetime import datetime
class BaseModel():
    """
    attributes and functions for BaseModel class
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__set_attr(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name,self.id,self.__dict__)

    def save(self):
        """
            private: converts attr_dict values to python class attributes
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    
    def to_dict(self):
        new_dict = {"__class__": type(self).__name__}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                new_dict[key] = datetime.isoformat(self.__dict__[key])
            else:
                new_dict[key] = self.__dict__[key]
        return new_dict
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
    
    def __set_attr(self, attr_dict):
        """
            private: converts attr_dict values to python class attributes
        """
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid.uuid4())
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



