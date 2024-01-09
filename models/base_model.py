#!/usr/bin/env python3

"""Define a baseclass to be used by a superclass by other classes"""

from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Creates an instance of base Model"""

    def __init__(self):
        """Instanciates the object"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints a user friendly output"""
        return f"{[__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """Updates the instance variable updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ instance
        """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
