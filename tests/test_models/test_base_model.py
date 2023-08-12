#!/usr/bin/python3
import unittest
"""unittest model for base_model.py"""
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel_init(unittest.TestCase):
    """Unittests for testing initiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """test __class__ type with no arg"""
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_id_is_str(self):
        """test public instance attributes id is str"""
        self.assertEqual(type(BaseModel().id), str)

    def test_created_at_is_datetime(self):
        """test public instance attributes created_at is datetime"""
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_updated_at_is_datetime(self):
        """test public instance attributes updated_at is datetime"""
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_id_is_unique(self):
        """test id created is unique for all init"""
        case0 = BaseModel()
        case1 = BaseModel()
        self.assertNotEqual(case1, case0)

    def test_upadted_at_created_at_init(self):
        """test updated_at and created at are equal on init"""
        case1 = BaseModel()
        self.assertEqual(case1.created_at, case1.updated_at)

    
class TestBaseModels_save(unittest.TestCase):
    """Unittests for testing Public instance methods save   of the BaseModel class."""

    def test_upadted_at_updates_on_save(self):
        """checks updated_at changes on save"""
        case0 = BaseModel()
        case0.save()
        self.assertNotEqual(case0.created_at, case0.updated_at)


if __name__ == "__main__":
    unittest.main()
