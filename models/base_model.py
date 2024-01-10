#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""
import uuid
from datetime import datetime
class BaseModel():
    def __init__(self):
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

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))