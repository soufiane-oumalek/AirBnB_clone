#!/usr/bin/python3
""" unit test for bases """
import json
import unittest
import pep8
from datetime import datetime
from models import storage
from models.base_model import BaseModel
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


class FileStorageTest(unittest.TestCase):
    """ class for save test """

    def test_pep8_compliance(self):
        """
        pycodestyle testing
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/engine/file_storage.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def test_storage(self):
        """
        storage test
        """
        for key in storage.all():
            self.assertTrue(eval(key.split(".\
")[0]) == storage.all()[key].__class__)


if __name__ == '__main__':
    unittest.main()
