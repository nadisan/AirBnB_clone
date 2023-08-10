#!/usr/bin/python3
"""Model that defines BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ defines all common attributes/methods for other classes"""

    def __init__(self, id=None, *args, **kwargs):
        """initialize class base"""

        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value,
                                                           date_format)
                else:
                    self.__dict__[key] = value

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
        """
        overides __str to print
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.to_dict())
