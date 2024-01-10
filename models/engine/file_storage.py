#!/usr/bin/python3
import json
from models import base_model
class FileStorage():
    """
        handles long term storage of all class instances
    """
    cls_init = {
        'BaseModel': base_model.BaseModel
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


