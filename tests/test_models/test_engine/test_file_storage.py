#!/usr/bin/python3
""" test model for file_storage.py"""
import pep8
import unittest
import os
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


class TestFileStorage_methoda(unittest.TestCase):
    """Unittests for testing all method of the FileStorage."""

    def testall_is_dict(self):
        """test __class__ type with no arg"""
        self.assertEqual(type(FileStorage().all()), dict)

    def test_new_all(self):
        """test new creates <obj class name>.id and is displayed by all"""
        base = BaseModel()

        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())

        with self.assertRaises(TypeError):
            models.storage.new(base, None)

    def test_save(self):
        """test save creates <obj class name>.id and is displayed by all"""
        base = BaseModel()

        models.storage.new(base)
        models.storage.save()
        save_test = ""

        with open("file.json", "r") as f:
            save_test = f.read()

        self.assertIn("BaseModel." + base.id, save_test)

        with self.assertRaises(TypeError):
            models.storage.save(base)

    def test_save_reload(self):
        """test save creates <obj class name>.id and is displayed by all"""
        new_f = FileStorage()

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(new_f.reload(), None)

        with self.assertRaises(TypeError):
            models.storage.reload(None)

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

   """ @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_style_check(self):"""
        """
        Tests pep8 style
        """
       """ style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")"""


    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

if __name__ == "__main__":
    unittest.main()
