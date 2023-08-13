#!/usr/bin/python3
""" unit test for bases """
import json
import unittest
import pep8
from datetime import datetime
from models import storage
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
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/engine/file_storage.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def test(self):
        """
        storage test
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/engine/file_storage.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def test___(self):
        """
        storage test
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/engine/file_storage.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def test_pe(self):
        """
        storage test
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/engine/file_storage.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def test_pep(self):
        """
        storage test
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/engine/file_storage.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)


if __name__ == '__main__':
    unittest.main()
