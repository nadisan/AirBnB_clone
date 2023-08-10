#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime
import json
import os
import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = {}
                    for k, v in value.items():
                        if k == 'created_at' or k == 'updated_at':
                            obj_dict[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                        else:
                            obj_dict[k] = v
                        obj = self.class_dict[value['__class__']](**value)
                        self.__objects[key] = obj
                    FileStorage.__objects[key] = obj
