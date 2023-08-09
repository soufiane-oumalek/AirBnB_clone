#!/usr/bin/python3
import json
from model import base_model


class FileStorage:

    __file_path = "save.json"
    __objects = {}

    def all(self):

        return self.__objects

    def new(self, obj):

        __objects[obj.id] = obj


    def save(self):

        dictionary = {}
        for key in __objects:
            dictionary[key] = __objects[key].to_dict()
        
    with open(__file_path, "w") as file:
        file.write(json.dumps(dictionary))

    def reload(self):
        
        try:
            with open(__file_path, "r") as file:
                dictionary = json.loads(file.read())
            for key in dictionary:
                if 
