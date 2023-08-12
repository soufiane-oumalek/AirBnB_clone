#!/usr/bin/python3
""" unit test for bases """
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
    """ class for base test """
    pass


if __name__ == '__main__':
    unittest.main()
