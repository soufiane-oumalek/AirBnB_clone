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
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self)
    dictionary = {}
    

        



soufiane = BaseModel()
soufiane.name = "soufiane"
soufiane.my_number = 93956
print(soufiane)
print(type(soufiane.id))
print(soufiane.created_at)
print(soufiane.updated_at)