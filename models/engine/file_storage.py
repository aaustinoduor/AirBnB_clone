"""Createas a class that serializes instances to a JSON file
and  deserializes JSON file to instances
"""
import json
from pathlib import Path


class FileStorage:
    """Creates a File storage instance

    Attributes:
        __file_path (str): path to the file to save objects to
        __object (dict): A dictionary of objects
    """

    __file_path = Path('~/Dev/Alx/Airbnb/AirBnB_clone/')
    __objects = {}

    def all(self):
        """Returns a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the __objects dict with a key <obj class name>.id"""
        id_value = obj.get('id')
        class_name = obj.get('__class__')
        if id_value is not None and class_name is not None:
            key = f"{class_name}.{id_value}"
            FileStorage.__objects[key] = obj
        else:
            raise KeyError()

    # def save(self):
    #     """Serializes a python object to json"""
    #     with open(FileStorage.__file_path, 'a+') as file:
    #         file.seek(0)  # allows for reading of the file
    #         json.dump(FileStorage.__objects, file)

    # def reload(self):
    #     """Deserializes json to python obj in __objects"""
    #     if FileStorage.__file_path.exists():
    #         with open(FileStorage.__file_path, 'r') as file:
    #             FileStorage.new(json.load(file))
