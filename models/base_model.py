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
