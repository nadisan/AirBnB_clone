#!/usr/bin/python3
""" test model for file_storage.py"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage_init(unittest.TestCase):
    """Unittests for testing initiation of the FileStorage class."""

    def test_no_args_instantiates(self):
        """test __class__ type with no arg"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def testFileStorage_file_path(self):
        """check path to the JSON file is file.json"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def testFileStorage_objects(self):
        """check the __object class attribute is string"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def testStorage_init(self):
        """check storage is initialized in models.__init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
