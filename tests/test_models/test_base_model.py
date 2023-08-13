#!/usr/bin/python3
"""
basemodel unittest
"""
import unittest
import subprocess
import pep8
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTest(unittest.TestCase):
    """
    Base Test class
    """
    def test_pep8_compliance(self):
        """
        pycodestyle testing
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/base_model.py",
                                          "models/__init__.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def test_all(self):
        """
        test all even if there is no
        point of testing it
        """
        for key in storage.all():
            self.assertTrue(eval(key.split(".\
")[0]) == storage.all()[key].__class__)

    def test_unique_id(self):
        """
        test if two obj has two different ids
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


if __name__ == '__main__':
    unittest.main()
