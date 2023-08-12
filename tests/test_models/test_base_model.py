#!/usr/bin/python3
"""
basemodel unittest
"""
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """
    Base Test class
    """
    pass


if __name__ == '__main__':
    unittest.main()
