#!/usr/bin/python3
"""Model that defines BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """initialize class base"""

        Date_F = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, Date_F)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = type(self).__name__
        dict_copy.pop('_sa_instance_state', None)
        return dict_copy

    def __str__(self):
        """overriding the __str__ method"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
