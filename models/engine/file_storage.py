#!/usr/bin/python3
"""Model that save objects to a json file amd reload to python file"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
import json
import os
import models


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "State": State, "City": City, "Amenity": Amenity,
                  "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __obijects
        if the JSON file (__file_path) exists
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = {}
                    for k, v in value.items():
                        if k == 'created_at' or k == 'updated_at':
                            obj_dict[k] = datetime.strptime
                            (v, '%Y-%m-%dT%H:%M:%S.%f')
                        else:
                            obj_dict[k] = v
                        obj = self.class_dict[value['__class__']](**value)
                        self.__objects[key] = obj
                    FileStorage.__objects[key] = obj
