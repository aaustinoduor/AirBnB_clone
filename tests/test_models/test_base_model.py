"""Tests the Base class BaseModel and it functionalities"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests the various  methods and attribiutes
    of the class
    """

    def setUp(self):
        """Instanciated objects to be used by the tests"""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def test_Instanciation(self):
        """Test objects are Not null on Instanciation"""
        self.assertIsNotNone(self.obj1)
        self.assertIsNotNone(self.obj2)
        self.assertIsInstance(self.obj1, BaseModel)
        self.assertIsInstance(self.obj2, BaseModel)

    def test_id(self):
        """Test unique id creation"""
        self.assertIsInstance(self.obj1.id, str)
        # self.assertIsInstance(self.obj2.id, uuid)
        self.assertNotEqual(self.obj1.id, self.obj2.id)

    def test_creation_time(self):
        """Tests time of instanciation is added"""
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj2.created_at, datetime)
        self.assertNotEqual(self.obj1.created_at, self.obj2.created_at)

    def test_updated_at(self):
        """Tests update time when an object is instanciated"""
        self.assertIsInstance(self.obj2.updated_at, datetime)

    def test_string_special_method(self):
        """Tests the string special method returns the correct output"""
        self.assertEqual(str(self.obj1), self.obj1.__str__())
        self.assertEqual(str(self.obj2), self.obj2.__str__())

    def test_save(self):
        """Tests if the instance attribute updated_at is updated
        with the current time
        """
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)
        self.obj1.save()
        self.assertNotEqual(self.obj1.created_at, self.obj1.updated_at)

    def test_to_dict(self):
        """Test whether all instance key values are present
         and in the right format"""
        my_dict = self.obj2.to_dict()

        self.assertIsNotNone(my_dict)
        self.assertIn('__class__', my_dict)
        self.assertIsInstance(my_dict['created_at'], str)
        self.assertIsInstance(my_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
