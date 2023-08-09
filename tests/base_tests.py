#!/usr/bin/python3
""" 0-unittest """
import unittest
from models.base_model import BaseModel

class TestBase(unittest.TestCase):

    def test(self):
        b1 = BaseModel()
        self.assertEqual(type(b1.id), "<class 'str'>")

if __name__ == '__main__':
    unittest.main()
