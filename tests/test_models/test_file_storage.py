import unittest
# from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
# import json


class TestFileStorage(unittest.TestCase):
    """Test attributes and methods of class instances"""

    def setUp(self):
        """Set up objects to be used by all tests"""
        self.obj1 = FileStorage()
        self.obj2 = FileStorage()

    def test_private_class_Attr_file_path(self):
        """Ascertains the private class attribute is actually private"""
        with self.assertRaises(AttributeError):
            self.assertIsInstance(self.obj1.__objects, str)

        with self.assertRaises(AttributeError):
            self.assertIsInstance(FileStorage.__objects, str)

    def test_private_class_Attr_objects(self):
        """Ascertains the private attribute is actually private"""
        with self.assertRaises(AttributeError):
            self.assertIsInstance(self.obj2.__objects, dict)

        with self.assertRaises(AttributeError):
            self.assertIsInstance(FileStorage.__objects, dict)

    def test_all_method(self):
        """Test the function returns a dictionary object"""
        self.assertIsInstance(self.obj1.all(), dict)
        self.assertIsNotNone(self.obj2.all())

    def test_new_method_with_valid_object(self):
        """Ascertains the method new, adds valid objects to the private class attribute"""
        my_obj1 = BaseModel().to_dict()
        my_obj2 = BaseModel().to_dict()
        self.assertIsInstance(my_obj1, dict)
        key1 = f"{my_obj1.get('__class__')}.{my_obj1.get('id')}"
        key2 = f"{my_obj2.get('__class__')}.{my_obj2.get('id')}"
        self.obj1.new(my_obj1)
        self.obj2.new(my_obj2)
        self.assertIn(key1, FileStorage._FileStorage__objects)
        self.assertIn(key2, FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key1], my_obj1)
        # name mangling used to access the attr object
        self.assertEqual(FileStorage._FileStorage__objects[key2], my_obj2)

    def test_new_method_with_invalid_object(self):
        """Ascertains invalid objects are not added to the dictionary object"""
        my_obj1 = BaseModel().to_dict()
        del my_obj1['__class__']
        # self.assertIn('__class__', my_obj1)
        my_obj2 = BaseModel().to_dict()
        del my_obj2['id']

        with self.assertRaises(KeyError):
            self.obj1.new(my_obj1)

        with self.assertRaises(KeyError):
            self.obj2.new(my_obj2)

    # TODO: write tests for methods save and reload
    # def test_save_method(self):
    #     """Test the method serializes a python obj to json"""
    #     my_obj = BaseModel().to_dict()
    #     self.obj1.save(my_obj)
    #     pass

    # def test_reload_method(self):
    #     """"Ascertain whether the method converst json to python objects
    #     and saves them in __objects
    #     """
    #     my_obj = BaseModel().to_dict()
    #     self.obj1.reload(json.dumps(my_obj))
    #     self.assertIsEqual(FileStorage._FileStorage__objects,)
    #     pass


if __name__ == "__main__":
    unittest.main()
