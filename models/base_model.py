#!/usr/bin/python3
#defines all common attributes/methods for other classes
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    initilization class """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
