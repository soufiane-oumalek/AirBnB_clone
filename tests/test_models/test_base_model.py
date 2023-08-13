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


# class BaseModelTest(unittest.TestCase):
#     """
#     Base Test class
#     """
#     def test_pep8_compliance(self):
#         """
#         pycodestyle testing
#         """
#         pycodestyle = pep8.StyleGuide(quiet=True)
#         result = pycodestyle.check_files(["models/base_model.py",
#                                           "models/__init__.py"])
#         errorMessage = "Found code style errors (and warnings)."
#         self.assertEqual(result.total_errors, 0, errorMessage)

#     def test_all(self):
#         """
#         test all even if there is no
#         point of testing it
#         """
#         for key in storage.all():
#             self.assertTrue(eval(key.split(".\
# ")[0]) == storage.all()[key].__class__)

#     def test_instance(self):
#         """Testing a new created instance"""
#         obj = BaseModel()
#         self.assertEqual(BaseModel, type(obj))

#     def test_instance_id(self):
#         obj = BaseModel()
#         self.assertEqual(str, type(obj.id))

#     def test_obj_id(self):
#         obj = BaseModel()
#         self.assertEqual(datetime, type(obj.created_at))

#     def test_unique_id(self):
#         """
#         test if two obj has two different ids
#         """
#         bm1 = BaseModel()
#         bm2 = BaseModel()
#         self.assertNotEqual(bm1.id, bm2.id)

#     def test_obj_str(self):
#         obj = BaseModel()
#         expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
#         self.assertEqual(expected_str, obj.__str__())

#     def test_obj_created_at(self):
#         obj = BaseModel()
#         self.assertEqual(datetime, type(obj.created_at))

#     def test_object_to_dict(self):
#         """Testing To_dict method"""
#         instance = BaseModel()
#         instance.name = "My First Model"
#         instance.my_number = 89
#         dictionary = instance.to_dict()
#         dictionary_cmp = {
#             'my_number': 89,
#             'name': 'My First Model',
#             '__class__': 'BaseModel',
#             'updated_at': instance.updated_at.isoformat(),
#             'id': instance.id,
#             'created_at': instance.created_at.isoformat()
#         }
#         self.assertEqual(dictionary_cmp, dictionary)

#     def test_instance_init_kwargs(self):
#         """Testing kwargs"""
#         instance = BaseModel()
#         instance.name = "My First Model"
#         instance.my_number = 89
#         self.assertEqual(instance.name, "My First Model")
#         self.assertEqual(instance.my_number, 89)

class TestBaseModel(unittest.TestCase):
    """
    TESTING CLASS
    """

    def test_instance(self):
        """Testing a new created instance"""
        instance = BaseModel()
        self.assertEqual(BaseModel, type(instance))

    def test_instance_id(self):
        instance = BaseModel()
        self.assertEqual(str, type(instance.id))

    def test_instance_id(self):
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))

    def test_instance_id_unique(self):
        instance_1 = BaseModel()
        instance_2 = BaseModel()
        self.assertNotEqual(instance_1.id, instance_2.id)

    def test_instance_str(self):
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(expected_str, instance.__str__())

    def test_instance_created_at(self):
        instance = BaseModel()
        self.assertEqual(datetime, type(instance.created_at))
    def test_object_to_dict(self):
        """Testing To_dict method"""
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        dictionary = instance.to_dict()
        dictionary_cmp = {
            'my_number': 89,
            'name': 'My First Model',
            '__class__': 'BaseModel',
            'updated_at': instance.updated_at.isoformat(),
            'id': instance.id,
            'created_at': instance.created_at.isoformat()
        }
        self.assertEqual(dictionary_cmp, dictionary)

    def test_instance_init_kwargs(self):
        """Testing kwargs"""
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        self.assertEqual(instance.name, "My First Model")
        self.assertEqual(instance.my_number, 89)


if __name__ == '__main__':
    unittest.main()
