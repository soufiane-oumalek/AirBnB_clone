#!/usr/bin/python3
"""
base model of our HBnB
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Define BaseModel class
    """

    def __init__(self):
        """
        Initializes the `BaseModel` object.

        Attributes:
            id (str): The unique identifier of the object.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        string method that return descriptor of the object
        Return:
            object descriptor
        """
        return ("[{}] ({}) {}\
".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save method that save time update and update
        the updated_at instance attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict method that get an prepared dict
        Return:
            new dictionary
        """
        dictionary = {}
        for key in self.__dict__:
            dictionary[key] = self.__dict__[key]
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
