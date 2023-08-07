#!/usr/bin/python3
""" Model for  base class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, id=None):
        """initialize class base"""
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """overriding the __str__ method"""
        return "[{:s}] ({:s}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Saving update time"""
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic

