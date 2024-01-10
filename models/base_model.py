#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""
from typing import Any
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
    def __str__(self):
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name,self.id,self.__dict__)
    def save(self):
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        new_dict = {"__class__": type(self).__name__}
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                new_dict[key] = datetime.isoformat(self.__dict__[key])
            else:
                x = self.id
                new_dict[key] = x
        return new_dict
    
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



my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)