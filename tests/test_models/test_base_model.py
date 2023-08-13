#!/usr/bin/python3
"""
basemodel unittest
"""
import unittest
import subprocess
import pep8
from models.base_model import BaseModel
from datetime import datetime
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


if __name__ == '__main__':
    unittest.main()
