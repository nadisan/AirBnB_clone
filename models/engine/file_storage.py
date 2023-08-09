#!/usr/bin/python3
"""Model to save a file"""
from models.base_model import BaseModel
import os
import json


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ saves new obj"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open (self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to __objects if it exists"""
        try:
            with open (self.__file_path, "r", encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key,value in new_obj_dict.items():
                class_name, obj_id = key.split(".")
                obj_class = models.classes[class_name]
                print(obj_class)
                obj = obj_class(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
        except json.JSONDecodeError as e:
            print(f"Error while decoding JSON data: {e}i")
